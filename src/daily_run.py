import os
import json
import rule_library_username as rule_library
import get_data as get_data
from measure_build import * 
import torch
from function_library import *
from rule_build import *
import analysis as analysis
import build_upload as build_upload
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=UserWarning)

strategy_name_list = ['combine_rule_long_172','combine_rule_short_135']
rule_list = [] # 有用到那些rule
measure_list = [] # 有用到那些measure

for run_strategy_name in strategy_name_list:
    folder_name = 'combine_rule_single' if 'single' in run_strategy_name else 'combine_rule'
    longshort = 'long' if 'long' in run_strategy_name else 'short'
    strategy_index = run_strategy_name.split("_")[-1]
    print()
    json_files = os.path.join(folder_name,f"{folder_name}_{longshort}_{strategy_index}",f"{folder_name}_{longshort}_{strategy_index}.json")
    with open(json_files, 'r', encoding='utf-8') as file:
        combined_rule_info = json.load(file)
        for rule in combined_rule_info['rule_use']:
            rule_list.append(rule) 
            obj_rule = rule_library.Rule_Library()
            rule_method = getattr(obj_rule, rule, None)
            rule_method()
            for measure in obj_rule.get_cross_section_data_file_name():
                measure_list.append(measure)
    save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'raw_data')
measure_list = list(set(measure_list))
rule_list = list(set(rule_list))
# 抓資料
for symbol in measure_list:
    obj = get_data.Crawl_data(
        name = symbol,
        observation_start = "2005-01-01",
        realtime_start="1999-01-01",
        days=1
        )
    df = obj.get_fred_data()
    df.to_csv(os.path.join(save_path,f"{symbol}.csv"),encoding = 'utf-8-sig')
# 建立measure
data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'raw_data')
save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'measure')
symbol_files_list = [x + ".csv" for x in measure_list]
if 1: # 製作 *.pt
    create_tensor(symbol_files_list,data_path = data_path,save_path = save_path)
    
# 建立rule

print(f"-----建立rule-----")
measure_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'measure')
rule_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'rule')

for rule_name in rule_list:
    obj_rule = rule_library.Rule_Library()
    exec(f"obj_rule.{rule_name}()")
    # data_dictionary  {'變數名稱':內容}
    data_dictionary = load_data_dictionary(keys=obj_rule.cross_section_data,file_ext = 'pt',
                                            filenames=obj_rule.cross_section_data_file_name,
                                            data_dir = os.path.join(measure_path))
    result_signal = rule_calculate(obj_rule.get_process_variable(),**data_dictionary)
    print(f"建立 {rule_name}") 
    signal_count_check_input_result(result_signal)# 檢核 確認有沒有效
    save_tensor(result_signal, os.path.join(rule_path,rule_name + ".pt"),method = 'hdf5')
    print("-"*50)
print(f"-----分析-----")
obj_RunEvaluate = analysis.RunEvaluate()
obj_RunEvaluate.main_for_combine_rule(given_strategy_name = strategy_name_list) # 合併的rule
obj_RunEvaluate.build_combine_table(given_strategy_name = strategy_name_list)


for strategy_name in strategy_name_list:
    obj_buildupload_data = build_upload.BuildUploadData(strategy_name)
    obj_buildupload_data.run()
    upload = obj_buildupload_data.upload(strategy_name)
    