import pandas as pd
import os
import random
import json

class RuleCombiner:
    def __init__(self, long_file, short_file, save_dir='combine_rule', num_combinations=100, max_rules=5):
        self.long_file = long_file
        self.short_file = short_file
        self.save_dir = save_dir
        self.num_combinations = num_combinations
        self.max_rules = max_rules
        os.makedirs(self.save_dir, exist_ok=True)

    def load_data(self, file_path):
        try:
            # 讀取 CSV 並選取必要的欄位
            path =os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'data')
            df = pd.read_csv(os.path.join(path,file_path), encoding='utf-8-sig')
            selected_columns = ['measure_list', 'combined_rule', 'rule_descriptions', 'accuracy', 'precision', 'recall', 'f1_score','rule_number']
            df.loc[:, 'rule_number'] = df['combined_rule'].str.extract(r'(\d+)').astype(int)

            sample_data = df[selected_columns]

            # 按 rule_number 排序
            sample_data = sample_data.sort_values(by='rule_number').reset_index(drop=True)

            return sample_data
        except FileNotFoundError:
            raise Exception(f"檔案 {file_path} 不存在")
        except KeyError as e:
            raise Exception(f"缺少必要欄位: {e}")

    def generate_combinations(self, df):
        if len(df) < - 1:
            raise ValueError("資料不足以抽取至少 1 個規則")

        combinations = []
        for _ in range(self.num_combinations):
            num_rules = random.randint(2, self.max_rules)  # 隨機選擇 2 到 max_rules 個規則
            sample_rules = df.sample(n=num_rules)

            # 按照 rule 編號排序
            # sample_rules = sample_rules.sort_values(by='rule_number', key=lambda x: x.str.extract(r'(\d+)', expand=False).astype(int))
            sample_rules = sample_rules.sort_values(by='rule_number', key=lambda x: x.astype(int))

            # 設定每個 rule 的權重
            weight = 1 / num_rules
            sample_rules['weight'] = weight

            # 整理成目標 JSON 格式
            combination = {
                "rule_use": [eval(_)[0] for _ in sample_rules['combined_rule']],
                "rule_weight": [weight] * num_rules,
                "rule_describe": [eval(_)[0] for _ in sample_rules['rule_descriptions']]
            }
            combinations.append(combination)
        return combinations

    def save_combinations(self, combinations, folder_prefix):
        path =os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'data')
        
        for i, combination in enumerate(combinations):
            
            folder_name = os.path.join(path,self.save_dir, f"{folder_prefix}_{i+1}")
            os.makedirs(folder_name, exist_ok=True)

            # 保存為 JSON 檔案
            json_file_path = os.path.join(folder_name, f"{folder_prefix}_{i+1}.json")
            print(f"建立檔案{json_file_path}")
            with open(json_file_path, 'w', encoding='utf-8') as json_file:
                json.dump(combination, json_file, ensure_ascii=False, indent=4)

    def create_long_short_combinations(self):
        # 分別生成和保存 long 和 short 的組合
        for file_path, label in zip([self.long_file, self.short_file], ["long", "short"]):
            data = self.load_data(os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'data'),'output_table',file_path))
            combinations = self.generate_combinations(data)
            self.save_combinations(combinations, f"combine_rule_{label}")
        print("Long and Short combinations have been saved successfully.")


if __name__ == '__main__':
    long_file_path = 'single_table_long.csv'
    short_file_path = 'single_table_short.csv'
    combiner = RuleCombiner(long_file=long_file_path, short_file=short_file_path,num_combinations = 15, max_rules=5)
    combiner.create_long_short_combinations()
