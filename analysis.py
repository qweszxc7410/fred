import os
import pandas as pd
import json
import numpy as np
import torch
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from function_library import load_tensor, load_pickle
import rule_library_username as rule_library
import re

class RuleEvaluator:
    def __init__(self, signal_file_name, combined_rule_info, output_folder_name, rule_index, longshort, device='cpu',strategy_name = None):
        self.df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)),signal_file_name), encoding='utf-8-sig')
        self.output_folder_name = output_folder_name
        self.rule_index = rule_index
        self.longshort = longshort
        self.device = device  # 設置運算設備 (cpu/cuda)
        self.strategy_name = strategy_name
        self.evaluate_combined_rule(self.df, combined_rule_info)
    # 定義一個函數來計算區間數量並檢查 rule_score 是否有訊號
    @staticmethod
    def count_intervals_with_signal(df,interval_column, rule_column):
        series = df[interval_column]
        rule_series = df[rule_column]
        
        # 找出區間起點 (從 0 變為 1)
        start_points = (series.shift(1, fill_value=0) == 0) & (series == 1)
        # 找出區間終點 (從 1 變為 0)
        end_points = (series.shift(-1, fill_value=0) == 0) & (series == 1)
        
        # 統計每個區間是否符合條件
        intervals = []
        rule_signals = []
        interval_ranges = []  # 用來記錄區間範圍
        signal_ranges = []    # 用來記錄有訊號的區間範圍
        start_idx = None
        for idx, value in enumerate(series):
            if start_points.iloc[idx]:
                start_idx = idx
            if end_points.iloc[idx] and start_idx is not None:
                # 區間的範圍
                interval_range = (df.index[start_idx].strftime('%Y-%m-%d'), df.index[idx].strftime('%Y-%m-%d'))
                interval_ranges.append(interval_range)
                # 確認區間內的 interval_column 是否全為 1
                intervals.append(series.iloc[start_idx:idx + 1].any())
                # 確認區間內的 rule_column 是否全為非零
                rule_signals.append((rule_series.iloc[start_idx:idx + 1] != 0).any())
                has_signal = (rule_series.iloc[start_idx:idx + 1] != 0).any()
                if has_signal:
                    signal_ranges.append(interval_range)
                start_idx = None
        
        # 總區間數量、全為 1 的區間數量、有訊號的區間數量
        total_intervals = len(intervals)
        signal_intervals = sum(rule_signals)
        return total_intervals,  signal_intervals,interval_ranges, signal_ranges
    @staticmethod
    def evaluate_rule(strategy_name,merged_df,longshort,measure_name_list, rule_use_list,rule_describe_list,rule_weight_list):
        # 設置 y_pred 和 y_true
        y_pred = merged_df['y_pred']
        y_true = merged_df['波段低點區間'] if longshort == 'long' else merged_df['波段高點區間']
        if longshort.lower() == 'long': 
            count_intervals_with_signal_result = RuleEvaluator.count_intervals_with_signal(merged_df,'波段低點區間', 'y_pred')
        else:
            count_intervals_with_signal_result = RuleEvaluator.count_intervals_with_signal(merged_df,'波段高點區間', 'y_pred')
        # 計算評估指標
        if int(count_intervals_with_signal_result[1]) == 0:
            signal_start_date = "-"
            signal_end_date = "-"
        else:
            signal_start_date = merged_df[merged_df.loc[:,'y_pred']!=0].index[0].strftime('%Y-%m-%d')
            signal_end_date = merged_df[merged_df.loc[:,'y_pred']!=0].index[-1].strftime('%Y-%m-%d')
        hit_low = int(sum(merged_df['y_pred'] * merged_df['波段低點區間']))
        not_hit_low = int(((merged_df['y_pred'] - merged_df['波段低點區間']) == 1).sum())
        hit_up =  int(sum(merged_df['y_pred'] * merged_df['波段高點區間']))
        not_hit_up = int(((merged_df['y_pred'] - merged_df['波段高點區間']) == 1).sum())
        
        results = {
            'measure_name': list(set(measure_name_list)),
            'measure_list': measure_name_list,
            'combined_rule': rule_use_list,
            'rule_descriptions': rule_describe_list,
            'rule_weight': rule_weight_list,
            'accuracy': accuracy_score(y_true, y_pred),
            'precision': precision_score(y_true, y_pred, zero_division=0),
            'recall': recall_score(y_true, y_pred, zero_division=0),
            'f1_score': f1_score(y_true, y_pred, zero_division=0),
            'longshort': longshort,
            'strategy_name': strategy_name,
            'count_0': int(len(y_pred) - y_pred.sum()),
            'count_1': int(y_pred.sum()),
            '區間數量': int(count_intervals_with_signal_result[0]),
            '幾個區間有訊號': int(count_intervals_with_signal_result[1]),
            '標註區間日期': count_intervals_with_signal_result[2],
            '訊號區間日期': count_intervals_with_signal_result[3],
            '分析日期起日': merged_df.index[0].strftime('%Y-%m-%d'),
            '分析日期迄日': merged_df.index[-1].strftime('%Y-%m-%d'),
            '標的':merged_df.columns[0],
            '訊號起日':signal_start_date,
            '訊號迄日':signal_end_date,
            '命中波段低點區間數量' : hit_low,
            '命中波段高點區間數量' : hit_up,
            '未命中波段低點區間數量': not_hit_low,
            '未命中波段高點區間數量': not_hit_up,
            '命中低點比率': round(hit_low/(hit_low + not_hit_low),4) if hit_low + not_hit_low != 0 else 0,
            '命中高點比率': round(hit_up/(hit_up + not_hit_up),4) if hit_up + not_hit_up != 0 else 0,
            '總分最大值':float(merged_df['rule_sum'].max()),
            '使用幾個Rule':len(rule_use_list),
            '使用幾個Measure':len(list(set(measure_name_list))),
            '未命中波段低點區間數量佔整體訊號比率': not_hit_low / int(y_pred.sum())  if int(y_pred.sum()) != 0 else 0,
            '未命中波段高點區間數量佔整體訊號比率': not_hit_up / int(y_pred.sum())  if int(y_pred.sum()) != 0 else 0,
            '命中低點比率減去未命中低點數量佔整體比率':  # 篩選指標
                round(hit_low/(hit_low + not_hit_low) - not_hit_low / int(y_pred.sum()),4) if int(y_pred.sum()) != 0 else 0,
            '命中高點比率減去未命中高點數量佔整體比率':  # 篩選指標
                round(hit_up/(hit_up + not_hit_up) - not_hit_up / int(y_pred.sum()),4) if int(y_pred.sum()) != 0 else 0,
        }
        return results

    def evaluate_combined_rule(self, df, combined_rule_info):
        df['Date'] = pd.to_datetime(df['Date'], format='%Y/%m/%d')
        df.set_index('Date', inplace=True)
        
        rule_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rule')
        measure_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'measure')

        # 從結構中提取數據
        rule_use = combined_rule_info["rule_use"]
        rule_weight = combined_rule_info["rule_weight"]
        rule_describe = combined_rule_info["rule_describe"]

        # 讀取並合併所有的規則數據
        obj_rule = rule_library.Rule_Library()
        measure_name_list = []
        measure_name_list_pure = []
        tensor_total = []

        
        for rule, weight in zip(rule_use, rule_weight):
            rule_method = getattr(obj_rule, rule, None)
            tensors = []
            
            if rule_method:
                rule_method()  # 如果需要參數，可以從 rule 中提取
                for _ in (obj_rule.cross_section_data_file_name):
                    measure_name_list_pure.append(_)
                measure_name_list.append(obj_rule.cross_section_data_file_name)
                _date = load_pickle(os.path.join(measure_path, obj_rule.cross_section_data_file_name[0] , obj_rule.cross_section_data_file_name[0] + "_date_list.pkl"))
                _date = pd.to_datetime(_date, format='%Y/%m/%d')
                tensor = load_tensor(os.path.join(rule_path, rule + ".pt"), method='hdf5')
                if len(tensor.shape) == 1:
                    tensor = tensor.unsqueeze(1)  # 將一維張量擴展為二維
                if tensor.shape[0] == len(_date):
                    date_to_tensor_index = {date: i for i, date in enumerate(_date)}
                    for current_date in df.index:
                        if current_date in date_to_tensor_index:
                            tensor_idx = date_to_tensor_index[current_date]
                            tensors.append(tensor[tensor_idx] * weight)  # 提取對應的 tensor 值
                        else:
                            tensors.append(torch.zeros(1))
                else:
                    print(f"警告: {rule} 的日期數據不匹配，請檢查。")
                tensor_total.append(torch.tensor(tensors))
        # 使用 AND 條件來合併張量（基於 PyTorch）
        combined_tensor = torch.stack(tensor_total, dim=1)
        combined_tensor_sum = combined_tensor.sum(axis= 1)
        condition = "over_threshold"
        threshold = 0.3
        if condition == "over_threshold":
            combined_tensor_score = (combined_tensor_sum > (threshold)) * 1  # 超過 0.8 是 1 分 # 0.8 太嚴苛了

        combined_tensor_score = combined_tensor_score.cpu().numpy().flatten()  # 確保結果為一維陣列
        tensor_df_score = pd.DataFrame(combined_tensor_score,index = df.index,columns = ['y_pred'])
        tensor_df_score_sum = pd.DataFrame(combined_tensor_sum,index = df.index,columns = ['rule_sum'])
        tensor_df_detail= pd.DataFrame(combined_tensor,index = df.index,columns = rule_use)
        
        merged_df = pd.merge(df, tensor_df_score, on='Date', how='left')
        merged_df = pd.merge(merged_df, tensor_df_score_sum, on='Date', how='left')
        merged_df = pd.merge(merged_df, tensor_df_detail, on='Date', how='left')
        
        merged_df[['波段低點區間', '波段高點區間']] = merged_df[['波段低點區間', '波段高點區間']].fillna(0)

        # RuleEvaluator.evaluate_rule(merged_df, rule_use)
        results = RuleEvaluator.evaluate_rule(self.strategy_name,merged_df,self.longshort,measure_name_list_pure, rule_use,rule_describe,rule_weight)

        # 創建對應的輸出資料夾，保持編號一致
        output_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),self.output_folder_name, f"{self.output_folder_name}_{self.longshort}_{self.rule_index}")
        os.makedirs(output_folder_path, exist_ok=True)

        # 將結果保存為 .json 檔案
        json_path = os.path.join(output_folder_path, f"{self.output_folder_name}_{self.longshort}_{self.rule_index}.json")
        with open(json_path, 'w', encoding='utf-8') as json_file:
            json.dump(results, json_file, ensure_ascii=False, indent=4)

        # 將結果保存為 .csv 檔案
        csv_path = os.path.join(output_folder_path, f"{self.output_folder_name}_{self.longshort}_{self.rule_index}.csv")
        pd.DataFrame([results]).to_csv(csv_path, encoding='utf-8-sig', index=False)
        merged_df.to_csv(os.path.join(output_folder_path, f"merged_df_{self.longshort}_{self.rule_index}.csv"), encoding='utf-8-sig', index=True)
        print(f"結果已保存至: {output_folder_path}")
class RunEvaluate:
    def __init__(self):...

    # 合併的rule
    def main_for_combine_rule(self,given_strategy_name = None):
        signal_file_name = "拐點標註檔.csv"
        output_folder = "output"
        path =os.path.join(os.path.dirname(os.path.abspath(__file__)))

        combine_rule_path = os.path.join(path,"combine_rule")
        if given_strategy_name is None:
            for prefix in ['combine_rule_long_', 'combine_rule_short_']:
                longshort = 'long' if 'long' in prefix else 'short'
                # if longshort == 'long':
                #     continue
                subfolders = [folder for folder in os.listdir(combine_rule_path) if folder.startswith(prefix)]

                for folder_name in subfolders:
                    folder_path = os.path.join(combine_rule_path, folder_name)

                    if os.path.exists(folder_path):
                        try:
                            rule_index = int(folder_name.split('_')[-1])
                        except ValueError:
                            print(f"錯誤: 無法從 {folder_name} 提取編號")
                            continue
                        # if int(folder_name.split("_")[-1]) < 201:
                        #     continue
                        json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
                        if json_files:
                            json_path = os.path.join(folder_path, json_files[0])
                            with open(json_path, 'r', encoding='utf-8') as file:
                                combined_rule_info = json.load(file)

                            print(f"處理 {folder_name}/{json_files[0]} 規則組合")
                            RuleEvaluator(
                                signal_file_name=signal_file_name,
                                combined_rule_info=combined_rule_info,
                                output_folder_name=output_folder,
                                rule_index=rule_index,
                                longshort=longshort,
                                device = 'cpu',
                                strategy_name =  json_files[0].split('.')[0]
                            )
        elif given_strategy_name is not None:
            for run_strategy_name in given_strategy_name:
                longshort = 'long' if 'long' in run_strategy_name else 'short'
                match = re.match(r'([a-zA-Z_]+?_rule(?:_[a-zA-Z]+)?)', run_strategy_name)
                folder_name =  match.group(1) if match else run_strategy_name
                if longshort in folder_name:
                    folder_name = folder_name.replace(f"_{longshort}",'')
                json_files = os.path.join(folder_name,run_strategy_name,f"{run_strategy_name}.json")
                with open(json_files, 'r', encoding='utf-8') as file:
                    combined_rule_info = json.load(file)

                RuleEvaluator(
                    signal_file_name=signal_file_name,
                    combined_rule_info=combined_rule_info,
                    output_folder_name=output_folder,
                    rule_index=run_strategy_name.split("_")[-1],
                    longshort=longshort,
                    device = 'cpu',
                    strategy_name =  json_files[0].split('.')[0]
                )
# 單一的rule
    def main_for_single_rule(self):
        signal_file_name = "拐點標註檔.csv"
        output_folder = "output_single"
        path =os.path.join(os.path.dirname(os.path.abspath(__file__)))

        rule_path = os.path.join(path,"rule")
        # 列出rule_path的檔案要是.pt結尾
        pt_files = [f for f in os.listdir(rule_path) if f.endswith(".pt")]
        save_path = os.path.join(path, "combine_rule_single")
        if 1:
            for longshort in ['long', 'short']:
                for filename in pt_files:
                    obj_rule = rule_library.Rule_Library()
                    rule_method = getattr(obj_rule, filename.split('.')[0], None)
                    rule_method()  # 如果需要參數，可以從 rule 中提取
                    json_result = {'rule_use':[filename.split('.')[0]], 'rule_weight':[1], 'rule_describe':[obj_rule.description]}
                    
                    rule_number = filename.split('.')[0].split('_')[-1]
                    folder_name = f"combine_rule_single_{longshort}_{rule_number}"
                    folder_path = os.path.join(save_path, folder_name)
                    os.makedirs(folder_path, exist_ok=True)
                    json_path = os.path.join(folder_path,f"combine_rule_single_{longshort}_{rule_number}.json")
                    with open(os.path.join(json_path), 'w', encoding='utf-8') as json_file:
                        json.dump(json_result, json_file, ensure_ascii=False, indent=4)
        
        os.makedirs(os.path.join(path, "output_single"), exist_ok=True)
        
        for prefix in ['combine_rule_single_long_', 'combine_rule_single_short_']:
            longshort = 'long' if 'long' in prefix else 'short'
            # if longshort == 'long':
            #     continue
            subfolders = [folder for folder in os.listdir(save_path) if folder.startswith(prefix)]

            for folder_name in subfolders:
                folder_path = os.path.join(os.path.join(save_path), folder_name)

                if os.path.exists(folder_path):
                    try:
                        rule_index = int(folder_name.split('_')[-1])
                    except ValueError:
                        print(f"錯誤: 無法從 {folder_name} 提取編號")
                        continue
                    # if int(folder_name.split("_")[-1]) < 201:
                    #     continue
                    json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
                    if json_files:
                        json_path = os.path.join(folder_path, json_files[0])
                        with open(json_path, 'r', encoding='utf-8') as file:
                            combined_rule_info = json.load(file)

                        print(f"處理 {folder_name}/{json_files[0]} 規則組合")
                        RuleEvaluator(
                            signal_file_name=signal_file_name,
                            combined_rule_info=combined_rule_info,
                            output_folder_name=output_folder,
                            rule_index=rule_index,
                            longshort=longshort,
                            device = 'cpu',
                            strategy_name =  json_files[0].split('.')[0],
                        )
                        
    def build_combine_table(self,only_sigle_rule = False,given_strategy_name = None):
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        # 資料價名稱output_long_1 # long short 分開執行
        combine_rule_list = []
        if given_strategy_name is None:
            for prefix in ['output_long_', 'output_short_']:
                for output_folder_name in ['output','output_single']:
                    if only_sigle_rule and output_folder_name == 'output':
                        continue
                    combine_rule_path = os.path.join(path, output_folder_name)
                    if output_folder_name=='output_single' and prefix == "output_long_":
                        prefix = "output_single_long_"
                    elif output_folder_name=='output_single' and prefix == "output_short_":
                        prefix = "output_single_short_"
                    
                    if os.path.exists(combine_rule_path):
                        subfolders = [folder for folder in os.listdir(combine_rule_path) if folder.startswith(prefix)]

                        for folder_name in subfolders:
                            folder_path = os.path.join(combine_rule_path, folder_name)

                            if os.path.exists(folder_path):
                                try:
                                    rule_index = int(folder_name.split('_')[-1])
                                except ValueError:
                                    print(f"錯誤: 無法從 {folder_name} 提取編號")
                                    continue

                                json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
                                if json_files:
                                    json_path = os.path.join(folder_path, json_files[0])
                                    with open(json_path, 'r', encoding='utf-8') as file:
                                        combined_rule_info = json.load(file)

                                    combine_rule_list.append(combined_rule_info)
                # 生成綜合表格
                longshort = 'long' if 'long' in prefix else 'short'
                combine_table = pd.DataFrame(combine_rule_list)
                # long short 分開成兩張表
                
                if only_sigle_rule:
                    print(f"存檔 {os.path.join(path, f'single_table_{longshort}.csv')}")
                    combine_table.loc[combine_table['longshort'] == longshort,:].to_csv(os.path.join(path, f"single_table_{longshort}.csv"), encoding='utf-8-sig', index=False)
                else:
                    print(f"存檔 {os.path.join(path, f'combine_table_{longshort}.csv')}")
                    combine_table.loc[combine_table['longshort'] == longshort,:].to_csv(os.path.join(path, f"combine_table_{longshort}.csv"), encoding='utf-8-sig', index=False)
                
        elif not given_strategy_name is None:
            for run_strategy_name in given_strategy_name:
                folder_name = 'output_single' if 'single' in run_strategy_name else 'output'
                longshort = 'long' if 'long' in run_strategy_name else 'short'
                strategy_index = run_strategy_name.split("_")[-1]
                json_files = os.path.join(folder_name,f"{folder_name}_{longshort}_{strategy_index}",f"{folder_name}_{longshort}_{strategy_index}.json")
                with open(json_files, 'r', encoding='utf-8') as file:
                    combined_rule_info = json.load(file)
                combine_rule_list.append(combined_rule_info)
            combine_table = pd.DataFrame(combine_rule_list)
            print(f"存檔 {os.path.join(path, f'combine_table_{longshort}.csv')}")
            combine_table.to_csv(os.path.join(path, f"combine_table_{longshort}.csv"), encoding='utf-8-sig', index=False)

                        
if __name__ == '__main__':
    
    if 0: #只跑組合的
        obj_RunEvaluate = RunEvaluate()
        obj_RunEvaluate.main_for_combine_rule() # 合併的rule
        obj_RunEvaluate.build_combine_table()
    if 0: #只跑單一的
        obj_RunEvaluate = RunEvaluate()
        obj_RunEvaluate.main_for_single_rule() # 單一rule 
        obj_RunEvaluate.build_combine_table(only_sigle_rule=True)
    if 0: # 組合 單一都跑
        obj_RunEvaluate = RunEvaluate()
        obj_RunEvaluate.main_for_combine_rule() # 合併的rule
        obj_RunEvaluate.main_for_single_rule() # 單一rule 
        obj_RunEvaluate.build_combine_table()
    if 1: # 組合 指定的
        run_strategy_name = ['combine_rule_long_2','combine_rule_single_long_1']
        obj_RunEvaluate = RunEvaluate()
        obj_RunEvaluate.main_for_combine_rule(given_strategy_name = run_strategy_name) # 合併的rule
        obj_RunEvaluate.build_combine_table(given_strategy_name = run_strategy_name)
        
        