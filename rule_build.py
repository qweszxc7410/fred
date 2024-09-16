import torch
from function_library import *
import os
import rule_library as rule_library
# GDPC1 = load_tensor(os.path.join('measure',"GDPC1","GDPC1" '.pt'),method='hdf5')
# # GDPC1[:,0,:][-1]
# obj_rule = rule_library.Rule_Library()
# obj_rule.rule_6()
# data_dictionary = {'GDPC1':GDPC1}
# print(obj_rule.get_process_variable())
# result_signal = rule_calculate(obj_rule.get_process_variable(),**data_dictionary)
# signal_count_check_input_command(obj_rule.get_process_variable(),**data_dictionary)
# print(result_signal.shape)
# print(result_signal[-10:,-1])
# obj_rule.rule_6()
# data_dictionary = {'GDPC1':GDPC1}
# print(obj_rule.get_process_variable())
# result_signa2 = rule_calculate(obj_rule.get_process_variable(),**data_dictionary)
# signal_count_check_input_command(obj_rule.get_process_variable(),**data_dictionary)
# print(result_signa2.shape)
# print(result_signa2[-10:,-1])
result = "rule_calculate(obj_rule.get_process_variable(), filled_tensor=filled_tensor)"
# print(obj_rule.get_process_variable())

def load_data_dictionary(keys, filenames, data_dir="", file_ext="", method='hdf5', loader=load_tensor):
    """
    載入多個檔案並建立一個資料字典。

    參數:
    - keys (list): 字典的鍵列表。
    - filenames (list): 對應每個鍵的檔案名稱列表。
    - data_dir (str): 檔案所在的資料夾路徑（可選）。
    - file_ext (str): 檔案副檔名（不含點，例如 'pt'，可選）。
    - method (str): 載入資料的方法（預設為 'hdf5'）。
    - loader (function): 用於載入單一檔案的函數（預設為 load_tensor）。

    回傳:
    - dict: 載入後的資料字典。
    """
    data_dict = {}
    for key, filename in zip(keys, filenames):
        try:
            # 構建完整的檔案路徑
            if file_ext:
                full_filename = f"{filename}.{file_ext}"
            else:
                full_filename = filename
            filepath = os.path.join(data_dir, filename , full_filename)
            
            # 載入資料
            data = loader(filepath, method=method)
            data_dict[key] = data
        except Exception as e:
            print(f"無法載入檔案 '{filepath}': {e}")
    return data_dict

if __name__ == '__main__':
    build_rule_list = ['rule_1','rule_2','rule_3','rule_4','rule_5','rule_6']
    # build_rule_list = ['rule_1','rule_2']
    
    print("-"*50)
    measure_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'measure')
    rule_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'rule')
    
    for rule_name in build_rule_list:
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
    pass