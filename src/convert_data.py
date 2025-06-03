
''' 取得資料只有資料日和值 沒有公布日 才使用 '''
import pandas as pd
from pandas.tseries.offsets import MonthEnd, QuarterEnd, YearEnd
import re
from pandas.tseries.offsets import MonthEnd, QuarterEnd, YearEnd, Week, Day
import numpy as np

class DateHandler:
    ''' 自動偵測頻率 並產新欄位 
    [頻率_自動判斷,頻率文字_自動判斷,Date_Auto_Adjustment]
    根據頻率調整日期 移動到月底 季底 年底
    '''
    frequency_mapping = {
        'D': 'Daily',
        'W': 'Weekly',
        'M': 'Monthly',
        'Q': 'Quarterly',
        'Y': 'Annualy',
        'H': 'SemiAnnually'
    }

    def auto_detect_freq(self, df, date_column):
        '''自定義推斷頻率並轉換日期到相應的結束日期'''
        frequency = self.custom_infer_freq(df[date_column])

        # 頻率
        translated_frequency = self.frequency_mapping.get(frequency, 'Unknown')
        df['頻率簡稱_自動判斷'] = frequency
        df['頻率完整名稱_自動判斷'] = translated_frequency

        # 根據頻率調整日期 移動到月底 季底 年底
        if frequency == 'D':  # 日
            df['Date_Auto_Adjustment'] = pd.to_datetime(df[date_column]) + Day(0)
        elif frequency == 'W':  # 週
            df['Date_Auto_Adjustment'] = pd.to_datetime(df[date_column]) + Week(0)
        elif frequency == 'M':  # 月
            df['Date_Auto_Adjustment'] = pd.to_datetime(df[date_column]) + MonthEnd(0)
        elif frequency == 'Q':  # 季
            df['Date_Auto_Adjustment'] = pd.to_datetime(df[date_column]) + QuarterEnd(0)
        elif frequency == 'Y':  # 年
            df['Date_Auto_Adjustment'] = pd.to_datetime(df[date_column]) + YearEnd(0)
        elif frequency == 'H':  # 半年
            df['Date_Auto_Adjustment'] = pd.to_datetime(df[date_column]) + MonthEnd(0)
        else:
            df['Date_Auto_Adjustment'] = np.nan
            print("DateHandler | Frequency not recognized, dates not adjusted.")
        return df

    @staticmethod
    def custom_infer_freq(dates):
        '''使用向量化運算自動選擇最接近的頻率'''
        dates = pd.to_datetime(dates)
        diff_days = dates.diff().dt.days  # 計算天數間隔
        diff_months = (diff_days / 30).dropna().to_numpy()  # 將天數差轉換為月數差，並轉換為NumPy陣列
        
        # 頻率標準間隔 (以月數為單位)
        freq_intervals = np.array([
            1 / 30,   # 每天 (1 天)
            7 / 30,   # 每週 (7 天)
            1,        # 每月 (30 天)
            3,        # 每季 (3 個月)
            6,        # 每半年 (6 個月)
            12        # 每年 (12 個月)
        ])
        
        # 計算每個間隔與所有標準頻率的距離
        distances = np.abs(diff_months[:, np.newaxis] - freq_intervals) # 增加一個新的維度 這樣才能做向量運算
        # 計算每列的平均距離，並選擇距離最小的頻率索引
        avg_distances = distances.mean(axis=0)
        closest_freq_index = np.argmin(avg_distances)

        # 對應頻率名稱
        freq_keys = ['D', 'W', 'M', 'Q', 'H', 'Y']
        closest_freq = freq_keys[closest_freq_index]

        return closest_freq
        
class ChangeFrequency():
    '''         for freq in freq_list:
            ChangeFrequency_instance = ChangeFrequency(data, change_freq=freq) 
            freq_list = ['D', 'W', 'M', 'Q']
            資料轉成 D W M Q ' 預設全部轉換
            原始檔案有紀錄 頻率 但不合理 不夠通用
    '''
    def __init__(self, data=None, days=None, change_freq_list = ['D', 'W', 'M', 'Q','2Q','Y'],data_freq=None):
        ''' 
        data : 輸入的是dataframe
        change_freq_list : 要轉換成的頻率
        data_freq : 資料頻率 可能有維護可能沒有
        '''
        self.data = data

        self.change_freq_list = change_freq_list
        self.data_freq = data_freq
        self.frequencies = {'日': 'D', '月': 'M', '季': 'Q', '半年': '2Q', '年': 'Y'}
        self.frequency_mapping = {'D': '日','M': '月','MS': '月','Q': '季','QS': '季','2Q': '半年', 'Y': '年', 'YS': '年'}
        

    
    @staticmethod
    def adjust_date(df, date_column = "Date_Auto_Adjustment", freq_column = "頻率簡稱_自動判斷", new_column='Date_Auto_Adjustment_Auto_Shift'):
        '''
        根據指定欄位中的頻率調整日期
        :param df: DataFrame 包含要調整的日期和頻率
        :param date_column: 要調整的日期欄位名稱
        :param freq_column: 包含頻率資訊的欄位名稱
        :return: 調整過日期的 DataFrame
        '''
        # 將日期列轉換為日期格式
        df[date_column] = pd.to_datetime(df[date_column])
        df[new_column] = df[date_column].copy()  # 使用copy確保不修改原始欄位 比較穩定
        
        # 掩碼處理不同頻率
        mask_D = df[freq_column] == 'D'
        mask_W = df[freq_column] == 'W'
        mask_M = df[freq_column] == 'M'
        mask_Q = df[freq_column] == 'Q'
        mask_H = df[freq_column] == 'H'
        mask_A = df[freq_column] == 'A'
        
        # 向量化操作調整日期到新的欄位
        df.loc[mask_D, new_column] = df.loc[mask_D, new_column] + Day(1)        # 日 - 往後一天
        df.loc[mask_W, new_column] = df.loc[mask_W, new_column] + Week(1)       # 週 - 往後一週
        df.loc[mask_M, new_column] = df.loc[mask_M, new_column] + MonthEnd(1)   # 月 - 往後一個月
        df.loc[mask_Q, new_column] = df.loc[mask_Q, new_column] + QuarterEnd(1) # 季 - 往後一季
        df.loc[mask_H, new_column] = df.loc[mask_H, new_column] + MonthEnd(6)   # 半年 - 往後六個月
        df.loc[mask_A, new_column] = df.loc[mask_A, new_column] + QuarterEnd(4) # 年 - 往後四個季

        return df


    def convert_all_frequency(self,df, date_column):
        ''' 都轉成日資料在平均可以反應大小月的差異 (每個月全種略有差異 但影響不大) '''
        ''' date_column 表示用哪個欄位轉換'''
        df[date_column] = pd.to_datetime(df[date_column])
        df = df.set_index(date_column)
        
        # 先將資料轉換為日資料
        df = df.resample('D').ffill()

        result = pd.DataFrame()
        
        for key, freq in self.frequencies.items():
            # 以特定頻率進行重新取樣並向前填補缺失值
            if 0:
                resampled_df = df.resample(freq).ffill()
            if 1:
                resampled_df = df.resample(freq).mean() # 以平均值取代

            # 輸出都是日曆日
            resampled_df = resampled_df.resample('D').ffill().reset_index()
            resampled_df.columns = ['Date', key]
            resampled_df.set_index('Date', inplace=True)
            result = pd.concat([result,resampled_df[[key]]], axis=1)
        
        return result

    def convert(self):
        for convert_freq in self.change_freq_list:
            print(f"Convert Freq to {convert_freq}")


if __name__ == '__main__':
    # 取得資料只有資料日和值 沒有公布日 才使用
    # 如果沒有給資料的公布日才用這個
    if 0:
        # file_name = 'M1SL_M1.csv'
        file_name = 'M1SL_M1_V2.csv'

        df = pd.read_csv(file_name,encoding = 'utf-8-sig')
        df = df.loc[:,['date','M1']]
        print(df.head(10))
        obj = ChangeFrequency()
        xx = ChangeFrequency.adjust_date(df)
        result = obj.convert_all_frequency(df,'date') # 依date欄位轉換
        result.to_csv(file_name.replace('.csv','_convert.csv'),encoding = 'utf-8-sig')
        
        # 自動偵測頻率
        obj.auto_detect_freq(df,'date')
    if 1:

        file_name = 'M1SL_M1_V3.csv'

        df = pd.read_csv(file_name,encoding = 'utf-8-sig')
        df = df.loc[:,['date','M1']] # 資料裡面的欄位 要用哪個欄位轉換和對應的日期 # 假設取得資料只有資料日和值 沒有公布日
        obj = DateHandler()
        new_df = obj.auto_detect_freq(df,'date')
        new_df = ChangeFrequency.adjust_date(new_df)
        new_df = new_df.loc[:,['Date_Auto_Adjustment_Auto_Shift','M1']]
        new_df.columns = ['date','value']
        print()
