import pandas as pd
import os
import shutil
import pygsheets
import time
import numpy as np
from dotenv import load_dotenv
import json
import base64
from google.oauth2.service_account import Credentials
import ast
import re
class BuildUploadData():

    def __init__(self, strategy_name):
        self.strategy_name_original = strategy_name
        self.strategy_name = strategy_name.replace('combine_rule','output') 
        self.path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'data')
        self.folder_name = "output_single" if 'single' in self.strategy_name else 'output'
        self.file_path = os.path.join(self.path,self.folder_name,self.strategy_name)
        self.file_name = self.strategy_name.replace('output_single','merged_df').replace('output','merged_df')
    @staticmethod
    def Upload2Gspread(data_path_str, target_sheetname, replace_values=True):
        load_dotenv()
        target_url = os.getenv("TARGET_URL")
        creds_json = os.getenv("GOOGLE_CREDENTIALS")
        if not creds_json:
            raise ValueError("環境變數 GOOGLE_CREDENTIALS 未設定")

        creds_dict = json.loads(base64.b64decode(creds_json).decode("utf-8"))
        credentials = Credentials.from_service_account_info(creds_dict, scopes=["https://www.googleapis.com/auth/spreadsheets"])
        gc = pygsheets.client.Client(credentials)
        output_wb = gc.open_by_url(target_url)
        output_sheet = output_wb.worksheet_by_title(target_sheetname)
        upload_data = pd.read_csv(data_path_str,encoding='utf-8-sig')

        upload_data.fillna(0, inplace=True)

        if replace_values:
            upload_data.replace([np.inf, -np.inf], -1, inplace=True)
            upload_data.replace(np.nan, -1, inplace=True)

        num_rows, num_cols = upload_data.shape
        
        # 自動擴展試算表行和列
        if output_sheet.rows < num_rows:
            output_sheet.add_rows(num_rows - output_sheet.rows)
        if output_sheet.cols < num_cols:
            output_sheet.add_cols(num_cols - output_sheet.cols)
        
        output_sheet.clear()
        
        # 分段上傳資料
        max_rows = 10000
        start_row = 0
        include_header = True  # 只有第一批包含標頭

        while start_row < len(upload_data):
            end_row = min(start_row + max_rows, len(upload_data))
            upload_chunk = upload_data.iloc[start_row:end_row].copy()
            
            # # 如果不是第一批次，移除標頭
            if not include_header:
                upload_chunk.columns = [''] * len(upload_chunk.columns)  

            success = False
            retries = 5
            backoff = 1
            
            while not success and retries > 0:
                try:
                    if include_header:
                        output_sheet.set_dataframe(upload_chunk, (start_row + 1, 1), include_index=False, nan='')
                        include_header = False  # Only include header in the first batch
                    else:
                        output_sheet.set_dataframe(upload_chunk, (start_row + 1, 1), include_index=False, nan='', copy_head=False)
                    success = True
                except Exception as e:
                    print(f"Error uploading chunk starting at row {start_row}: {e}")
                    time.sleep(backoff)
                    backoff *= 2
                    retries -= 1
            
            if not success:
                raise Exception(f"Failed to upload chunk starting at row {start_row} after multiple retries.")
            
            start_row = end_row  # 更新行起點
            time.sleep(1)

        print("Upload completed successfully.")
        return 0

                
    def run(self):
        df = pd.read_csv(os.path.join(self.file_path,self.file_name +'.csv'))
        print(df)
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df["Year"] = df["Date"].dt.year  # 新增年份欄位
        df["Week"] = df["Date"].dt.isocalendar().week  # 計算週數
        df["Month"] = df["Date"].dt.month  # 計算週數
        
        df = df[df["Date"].dt.year >= 2007]
        # 每兩周合併一次資料
        df["Week_group"] = (df["Week"] - 1) // 2  # 向下取整後，每兩周合併一次

        # 確保 Week 是基於 Year 和 Week_group 分組，避免跨年資料混淆
        df_last_per_two_weeks = df.sort_values("Date").groupby(["Year", "Week_group"]).last().reset_index()


        # 確保 Week 是基於 Year 分組，避免跨年資料混淆
        df_last_per_week = df.sort_values("Date").groupby(["Year", "Week"]).last().reset_index()
        df_last_per_month = df.sort_values("Date").groupby(["Year", "Month"]).last().reset_index()

        source_path = os.path.join(self.file_path, f"{self.strategy_name}.json")  # 請確保這裡是你的實際檔名

        # B 路徑（目標路徑）
        os.makedirs(os.path.join(self.path,'upload',self.strategy_name_original), exist_ok=True)
        destination_path = os.path.join(os.path.join(self.path,'upload',self.strategy_name_original), "info.json")
        df_last_per_month.to_csv(os.path.join(self.path,'upload',self.strategy_name_original, f"{self.strategy_name_original}.csv"), index=False)
        
        shutil.copy(source_path, destination_path) # 複製檔案並重新命名
        # 讀取 JSON 檔案
        with open(source_path, "r", encoding="utf-8") as file:
            json_data = json.load(file)
        items = list(json_data.items())

        # 建立 DataFrame，並指定欄位名稱
        df_new = pd.DataFrame(items, columns=['name', 'value'])
        df_new['value'] = df_new['value'].apply(lambda x: f"'{str(x)}")
        df_new.to_csv(os.path.join(os.path.join(self.path,'upload',self.strategy_name_original), "info.csv"), index=False, encoding="utf-8-sig")
        # 篩選出 'combined_rule' 和 'rule_descriptions' 兩列的數值
        combined_rule_values = df_new.loc[df_new['name'] == 'combined_rule', :].values
        rule_descriptions_values = df_new.loc[df_new['name'] == 'rule_descriptions', :].values
        rule_weight_values = df_new.loc[df_new['name'] == 'rule_weight', :].values
        # 將這兩列數據組合成一個字典
        # 假設這是您的資料，並確保它是字符串而不是 ndarray
        # value = str(combined_rule_values[0])  # 從 NumPy 陣列中提取單個值

        # # 去掉兩側的引號並解析為列表
        # parsed_list = ast.literal_eval(value.strip("'"))
        # # 提取數字部分並轉換為整數
        # numbers = []
        # for item in parsed_list:
        #     # 使用正則表達式提取數字部分
        #     match = re.search(r'(\d+)', item)  # 查找數字
        #     if match:
        #         numbers.append(int(match.group(1)))  # 將匹配到的數字轉換為整數並加入列表


        data = {
            'rule_id': combined_rule_values.flatten()[1:],  # 使用 flatten() 以確保數據是扁平化的
            'rule_descriptions': rule_descriptions_values.flatten()[1:],
            'rule_weight': rule_weight_values.flatten()[1:],
            'sort_id':eval((df_new.loc[df_new['name'] == 'combined_rule', :]['value'].values[0]).replace("rule_","").replace("'",""))
            
        }
        data_dict = {}

        # 將字典轉換為 DataFrame
        for key, value in data.items():
            # 使用 ast.literal_eval 來解析字符串格式的列表
            try:
                cleaned_value = value[0].strip("'")  # 去掉兩側的引號
                parsed_value = ast.literal_eval(cleaned_value)  # 解析為列表
            except:
                parsed_value = value  # 如果無法解析，則保留原始值
            # 將解析後的列表賦給data_dict字典，將key作為列名
            data_dict[key] = parsed_value

        # 將組合好的字典轉換為 DataFrame
        rule_description_df = pd.DataFrame(data_dict)

        rule_description_df.to_csv(os.path.join(os.path.join(self.path,'upload',self.strategy_name_original), "rule_description.csv"), index=False, encoding="utf-8-sig")
        print()

    def upload(self,strategy_name):
        path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'data')
        my_file_path= os.path.join(path,'upload',strategy_name,f'{strategy_name}.csv')
        target_sheetname='detail_long' if 'long' in strategy_name else 'detail_short'
        BuildUploadData.Upload2Gspread(my_file_path,target_sheetname, replace_values=False) 
        my_file_path= os.path.join(path,'upload',strategy_name,f'{"info"}.csv')
        target_sheetname='info_long' if 'long' in strategy_name else 'info_short'
        BuildUploadData.Upload2Gspread(my_file_path,target_sheetname, replace_values=False) 
        my_file_path= os.path.join(path,'upload',strategy_name,f'{"rule_description"}.csv')
        target_sheetname='rule_description_long' if 'long' in strategy_name else 'rule_description_short'
        BuildUploadData.Upload2Gspread(my_file_path,target_sheetname, replace_values=False) 
if __name__ == '__main__':

    strategy_name_list = ['output_long_1','output_short_3']
    
    for strategy_name in strategy_name_list:
        obj_buildupload_data = BuildUploadData(strategy_name)
        obj_buildupload_data.run()
        upload = obj_buildupload_data.upload(strategy_name)
        
    