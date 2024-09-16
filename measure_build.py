import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import torch
from function_library import * 
import os

def ffill_tensor(tensor_input,method = 2):
    # 確保 tensor_input 是浮點型態，才能處理 NaN
    tensor_input = tensor_input.float()

    mask = torch.isnan(tensor_input)  
    if method == 2:
        for k in range(1, tensor_input.shape[0]):  
            tensor_input[k, :, :] = torch.where(mask[k, :, :], tensor_input[k - 1, :, ], tensor_input[k, :, :])
    elif method ==1:

        for k in range(1, tensor_input.shape[0]):  
            tensor_input[:, :, k] = torch.where(mask[:, :, k], tensor_input[:, :, k-1], tensor_input[:, :, k])

    if 1: # 把未來資料變成nan 這樣避免以後的問題 # 做成下三角矩陣
        i_indices = torch.arange(tensor_input.shape[0]).view(-1, 1, 1)  # 形狀為 [i, 1, 1]
        k_indices = torch.arange(tensor_input.shape[2]).view(1, 1, -1)  # 形狀為 [1, 1, k]
        mask = k_indices > i_indices  # 形狀為 [i, 1, k] 建立一個遮罩來標記所有 k > i 的位置
        mask = mask.expand(tensor_input.shape[0], tensor_input.shape[1], -1)  # 將遮罩擴展
        # 使用遮罩將符合條件的位置填充為 NaN
        tensor_input[mask] = float('nan')
        # tensor_input[mask] = float(99999)
        
    # tensor_input = tensor_input.permute(2, 1, 0) # 把第一個維度和第三個維度互換 這樣操作比較合乎直覺  # 不互換前面程式都要改
    return tensor_input

def create_tensor(symbol_files,data_path = "",save_path = ""):
    
    for symbol_idx, file in enumerate(symbol_files):
        df = pd.read_csv(os.path.join(data_path,file),encoding = 'utf-8-sig')
        
        # 將所有錯誤的日期轉換為Nan
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        df['realtime_start'] = pd.to_datetime(df['realtime_start'], errors='coerce')
        df['realtime_end'] = pd.to_datetime(df['realtime_end'], errors='coerce')
        today = pd.Timestamp(datetime.now().date())  # 取得今天的日期
        
        # 將 Nan 的值替換為今天的日期
        df['date'].fillna(today, inplace=True)
        df['realtime_start'].fillna(today, inplace=True)
        df['realtime_end'].fillna(today, inplace=True)

        # 排序資料
        df = df.sort_values(by=['date', 'realtime_start', 'realtime_end'])
        max_date = max([df['date'].max(), df['realtime_start'].max(), df['realtime_end'].max()])
        min_date = min([df['date'].min(), df['realtime_start'].min(), df['realtime_end'].min()])
        if (df['realtime_start'][0] - df['date'][0] ).days > 500 : # 很晚才新增資料 才會有這麼大的差距 就採用自動修正
            # T10YFF
            df['realtime_start'] = df['date']

        # 建立日期範圍
        date_list = pd.date_range(start=min_date, end=max_date)
        if symbol_idx ==0:
            tensor = torch.full((len(date_list), len(symbol_files), len(date_list)), np.nan)
            date_tensor = torch.full((len(date_list), len(symbol_files), len(date_list)), np.nan, dtype=torch.float64)

        # 定義一個內部函數來查找位置
        def find_position(date):
            return date_list.get_loc(date)  # 使用 get_loc 方法查找索引
        
        # 為每個日期列創建新的位置列
        date_columns = ['realtime_start', 'realtime_end', 'date']
        for col in date_columns:
            df[f'{col}_position'] = df[col].apply(find_position)
            # 將資料填入 tensor 中
        for _, row in df.iterrows():
            start_pos = row['realtime_start_position']
            end_pos = row['realtime_end_position']
            date_pos = row['date_position']
            value = (row['value'])
            datadate = row['date']
            
            try:
                value = float(value)
            except ValueError:
                value = np.nan  # 使用 NaN 來替代無效值
            if 1:
                # 將指定範圍內的值填入 tensor
                tensor[start_pos:(end_pos+1), symbol_idx, date_pos] = value # 填值
                # date_tensor[start_pos:(end_pos+1), symbol_idx, date_pos] = int(datadate.strftime('%Y%m%d')) *  0.00000001 # 轉八碼填載小數位
                date_tensor[start_pos:(end_pos+1), symbol_idx, date_pos] = int(datadate.strftime('%Y%m%d')) *  0.0001 # 轉八碼填載小數位
                fillmethod = 1
            if 0:
                # 將指定範圍內的值填入 tensor
                tensor[date_pos, symbol_idx, start_pos:(end_pos+1)] = value # 填值
                # date_tensor[start_pos:(end_pos+1), symbol_idx, date_pos] = int(datadate.strftime('%Y%m%d')) *  0.00000001 # 轉八碼填載小數位
                date_tensor[date_pos, symbol_idx, start_pos:(end_pos+1)] = int(datadate.strftime('%Y%m%d')) *  0.0001 # 轉八碼填載小數位
                fillmethod = 2
                
        filled_tensor = ffill_tensor(tensor,method = fillmethod) # [:,0,:] 會是一個下三角的矩陣 但不會是從第一筆開始
        filled_tensor_date = ffill_tensor(date_tensor,method = fillmethod) # [:,0,:] 會是一個下三角的矩陣 但不會是從第一筆開始
        torch.equal(torch.nan_to_num(ffill_tensor(tensor,method = fillmethod),0.00), torch.nan_to_num(ffill_tensor(tensor,method = 3),0.00))
        
        # save file
        os.makedirs(os.path.join(save_path,file.split(".")[0]), exist_ok=True)
        save_tensor(filled_tensor,os.path.join(save_path,file.split(".")[0],file.split(".")[0]+ '.pt'),method='hdf5')
        save_tensor(filled_tensor_date,os.path.join(save_path,file.split(".")[0],file.split(".")[0]+ '_date.pt'),method='hdf5')
        # save_pickle(date_list,os.path.join(save_path,file.split(".")[0],file.split(".")[0]+ '_date_list.pkl'))
        
        df_sub = pd.DataFrame(filled_tensor[:, 0, :])
        # 設定 DataFrame 的索引和列名為 date_list
        df_sub.index = date_list  # 設置 index
        df_sub.columns = date_list  # 設置 columns
        output_path = os.path.join(save_path, file.split(".")[0], file.split(".")[0] + '.csv')
        df_sub.to_csv(output_path,encoding='utf-8-sig')
        
if __name__ == '__main__':
    # 使用示例
    
    data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'raw_data')
    save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'measure')
    symbol_files_list = ['GDPC1.csv']
    symbol_files_list = ['T10YFF.csv']
    if 1: # 製作GDPC1.pt
        create_tensor(symbol_files_list,data_path = data_path,save_path = save_path)
        # df = pd.DataFrame(data_tensor[:,0,:]) # 看這個比較好理解資料的樣子 第二個維度是因為只有一個symbol

