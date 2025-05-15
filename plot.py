import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib import rcParams
import matplotlib.dates as mdates

class Plot():
    def __init__(self, strategy_name):
        self.strategy_name = strategy_name.replace('output_','').replace('output_single','')
        folder_name = 'output_single' if 'single' in self.strategy_name else 'output'
        self.path = os.path.join(os.path.dirname(os.path.abspath(__file__)),folder_name)
        self.data= pd.read_csv(os.path.join(self.path, 'output' + "_" + self.strategy_name, "merged_df_" + self.strategy_name.replace("single_","") + ".csv"))
        self.longshort = 'long' if 'long' in self.strategy_name.lower() else 'short'
        print()
    def plot(self):
        rcParams['font.sans-serif'] = ['Microsoft JhengHei']  # 微軟正黑體
        rcParams['axes.unicode_minus'] = False  # 解決負號顯示問題

        self.data['Date'] = pd.to_datetime(self.data['Date'])
        # 繪圖
        plt.figure(figsize=(10, 6))

        # 繪製加權指數折線圖
        plt.plot(self.data['Date'], self.data['加權指數'], label='加權指數', color='blue', linewidth=1)

        # 加入底色：波段低點區間（淡紅色）
        if self.longshort == 'long':
            for idx, row in self.data.iterrows():
                if row['波段低點區間'] == 1:
                    plt.axvspan(row['Date'], row['Date'], color='lightcoral', alpha=0.5)
        if self.longshort == 'short':
            # 加入底色：波段高點區間（淡綠色）
            for idx, row in self.data.iterrows():
                if row['波段高點區間'] == 1:
                    plt.axvspan(row['Date'], row['Date'], color='lightgreen', alpha=0.5)

        # 標註紅色點：rule_score 為 1 的日期
        highlight_points = self.data[self.data['y_pred'] == 1]
        plt.scatter(highlight_points['Date'], highlight_points['加權指數'], color='red', label='Rule Score = 1', zorder=2, s=5)
        # 設置 X 軸為月份格式
        # 手動設置季度標籤
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
        plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=6))  # 每 3 個月顯示一次標籤

        # 設定圖例與標籤
        if self.longshort.lower() == 'long':
            longshort = "多頭"
        elif self.longshort.lower() == 'short':
            longshort = "空頭"
            
        plt.title(f'加權指數與{longshort}訊號 - {self.strategy_name}', fontsize=16)
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('加權指數', fontsize=12)
        plt.legend()
        plt.grid(alpha=0.3)
        plt.xticks(rotation=90)

        # 顯示圖表
        plt.tight_layout()
        # plt.show()
        # plt.close()
        print(f'存檔 {os.path.join(self.path, "output" + "_" + self.strategy_name, f"加權指數與{longshort}訊號 - {self.strategy_name}.png")}')
        plt.savefig(os.path.join(self.path, "output" + "_" + self.strategy_name, f"加權指數與{longshort}訊號 - {self.strategy_name}.png"))
if __name__ == '__main__':

    obj = Plot('output_single_long_1').plot() # 
    # output_long_2
    obj = Plot('output_long_2').plot() # 
    
    
    
    
    
    