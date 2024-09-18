import pandas as pd
from sklearn.metrics import  confusion_matrix ,accuracy_score, precision_score, recall_score, f1_score
from function_library import load_tensor,load_pickle
import os
import rule_library_username as rule_library_username
df = pd.read_csv('拐點標註檔.csv',encoding='utf-8-sig')

rule_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'rule')
measure_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'measure')
rule_list = ['rule_1','rule_2','rule_3','rule_4','rule_5','rule_6'] # 要分析哪些規則

results_list = []

for rule_name in rule_list:
    tensor = load_tensor(os.path.join(rule_path,rule_name + ".pt"),method = 'hdf5')
    date_list = load_pickle(os.path.join(measure_path,"GDPC1","GDPC1_date_list" + ".pkl"))


    df['Date'] = pd.to_datetime(df['Date'], format='%Y/%m/%d')
    date_df = pd.DataFrame({'Date': date_list})
    merged_df = pd.merge(date_df, df, on='Date', how='left')
    merged_df[['波段低點區間', '波段高點區間']] = merged_df[['波段低點區間', '波段高點區間']].fillna(0)
    assert tensor.shape[0] == len(date_list), "日期數量不一致"
    tensor_df = pd.DataFrame(tensor, columns=[rule_name])
    merged_df = pd.concat([merged_df, tensor_df], axis=1)

    assert tensor.shape[0] == merged_df.shape[0], "合併後日期大小改變"


    for lonshort in ['long','short']:
        result_dictionary_sub = {}
        if lonshort.lower() == 'long':        
            y_true = merged_df['波段低點區間']
        elif lonshort.lower() == 'short':
            y_true = merged_df['波段高點區間']
            
        y_pred = merged_df[rule_name]
        confusion_matrix_result = confusion_matrix(y_true,y_pred)
        accuracy = accuracy_score(y_true, y_pred)
        precision = precision_score(y_true, y_pred)
        recall = recall_score(y_true, y_pred)
        f1 = f1_score(y_true, y_pred)
        
        obj_rule = rule_library_username.Rule_Library()
        exec(f"obj_rule.{rule_name}()")
        
        result_dictionary_sub['start_date'] = merged_df['Date'].max()
        result_dictionary_sub['end_date'] = merged_df['Date'].min()
        result_dictionary_sub['LongShort'] = lonshort # 多空
        result_dictionary_sub['measure'] = obj_rule.cross_section_data_file_name
        result_dictionary_sub['rule'] = rule_name
        result_dictionary_sub['rule_describe'] = obj_rule.description
        
        result_dictionary_sub['accuracy'] = accuracy
        result_dictionary_sub['precision'] = precision # 重點
        result_dictionary_sub['recall'] = recall
        result_dictionary_sub['f1_score'] = f1
        result_dictionary_sub['signal_count_0'] = (y_pred == 0).sum()
        result_dictionary_sub['signal_count_1'] = (y_pred == 1).sum()
        results_list.append(result_dictionary_sub)
        
df = pd.DataFrame(results_list)
df.to_csv('bigtable.csv',encoding='utf-8-sig')
print()