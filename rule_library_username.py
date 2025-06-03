class Rule_Library():
    def __init__(self):...
    
    def get_cross_section_data(self):
        # 如果變數存在
        if hasattr(self,'cross_section_data'):
            return self.cross_section_data
        else:
            return []

    def get_rule_dataframe(self):
        return self.df

    def get_rule_list(self):
        return [method for method in dir(eval(type(self).__qualname__)) if not method.startswith('__')]

    def get_use_data(self):
        return self.use_data
        
    def get_rule_command(self):
        return self.rule_command
        
    def get_process_variable(self):
        return self.process_variable

    def get_use_data_by_cross_section_data(self):
        return self.use_data

    def get_cross_section_data_file_name(self):
        return self.cross_section_data_file_name

    def get_rule_description(self):
        return self.description
    # torch.diagonal(filled_tensor, dim1=0, dim2=2).T -> 當天看到的最新的GDP(過了就過了)
    ''' rule dmoe 

    '''
    def rule_1(self):
        # 描述
        self.description = "靜態美國GDP原始數字比250天前減少"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['GDPC1']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['GDPC1']

        # 處理變數
        self.process_variable = "diff_record_daily_value_change(GDPC1,windows = 250) < -  0 "

    
    def rule_2(self):
        # 描述
        self.description = "靜態美國GDP原始數字比250天前增加"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['GDPC1']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['GDPC1']

        # 處理變數
        self.process_variable = "diff_record_daily_value_change(GDPC1,windows = 250) > 0  "
    
    def rule_3(self):
        # 描述
        self.description = "動態美國GDP原始數字比250天前減少"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['GDPC1']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['GDPC1']

        # 處理變數
        self.process_variable = "diff_track_adjusted_values_change(GDPC1,windows = 60) <  0 "
    
    def rule_4(self):
        # 描述
        self.description = "動態美國GDP原始數字比250天前增加"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['GDPC1']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['GDPC1']

        # 處理變數
        self.process_variable = "diff_track_adjusted_values_change(GDPC1,windows = 250) > 0  "
        
    def rule_5(self):
        # 描述
        self.description = "動態美國GDP的250天變動幅度小於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['GDPC1']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['GDPC1']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(GDPC1,windows = 250) < 0.01 "
    
    def rule_6(self):
        # 描述
        self.description = "靜態美國GDP的250天變動幅度大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['GDPC1']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['GDPC1']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(GDPC1,windows = 250) > 0.01 "
        
    def rule_7(self):
        # 描述
        self.description = "動態美國GDP的250天變動幅度小於-10%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['GDPC1']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['GDPC1']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(GDPC1,windows = 250) < - 0.1 "

    def rule_8(self):
        # 描述
        self.description = "動態美國GDP的250天變動幅度大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['GDPC1']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['GDPC1']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(GDPC1,windows = 250) > 0.01 "

    def rule_9(self):
        # 描述
        self.description = "動態美國GDP的250天變動幅度大於5%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['GDPC1']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['GDPC1']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(GDPC1,windows = 250) > 0.05 "

    def rule_10(self):
        # 描述
        self.description = "動態美國GDP的250天變動幅度大於10%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['GDPC1']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['GDPC1']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(GDPC1,windows = 250) > 0.1 "
    
    def rule_11(self):
        # 描述
        self.description = "靜態美國GDP的250天變動幅度小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['GDPC1']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['GDPC1']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(GDPC1,windows = 250) < - 0.01 "

    def rule_12(self):
        # 描述
        self.description = "靜態美國GDP的250天變動幅度小於-5%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['GDPC1']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['GDPC1']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(GDPC1,windows = 250) < - 0.05 "

    def rule_13(self):
        # 描述
        self.description = "靜態美國GDP的250天變動幅度小於-10%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['GDPC1']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['GDPC1']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(GDPC1,windows = 250) < - 0.1 "

    def rule_14(self):
        # 描述
        self.description = "靜態美國GDP的250天變動幅度大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['GDPC1']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['GDPC1']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(GDPC1,windows = 250) > 0.01 "

    def rule_15(self):
        # 描述
        self.description = "靜態美國GDP的250天變動幅度大於5%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['GDPC1']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['GDPC1']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(GDPC1,windows = 250) > 0.05 "

    def rule_16(self):
        # 描述
        self.description = "靜態美國GDP的250天變動幅度大於10%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['GDPC1']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['GDPC1']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(GDPC1,windows = 250) > 0.1 "

    def rule_17(self):
        # 描述
        self.description = "靜態美國GDP的MOM大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['GDPC1']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['GDPC1']

        # 處理變數： 利用函數計算MOM增長
        self.process_variable = "percent_change_record_daily_value_change(GDPC1,windows = 30) > 0.01"

    def rule_18(self):
        # 描述
        self.description = "動態美國GDP的MOM大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['GDPC1']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['GDPC1']

        # 處理變數： 利用函數計算MOM增長
        self.process_variable = "percent_change_track_adjusted_values_change(GDPC1,windows = 30) > 0.01"

    def rule_19(self):
        # 描述
        self.description = "動態美國GDP的MOM大於5%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['GDPC1']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['GDPC1']

        # 處理變數： 利用函數計算MOM增長
        self.process_variable = "percent_change_track_adjusted_values_change(GDPC1,windows = 30) > 0.05"

    def rule_20(self):
        # 描述
        self.description = "動態美國GDP的MOM大於10%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['GDPC1']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['GDPC1']

        # 處理變數： 利用函數計算MOM增長
        self.process_variable = "percent_change_track_adjusted_values_change(GDPC1,windows = 30) > 0.10"

    def rule_21(self):
        # 描述
        self.description = "動態美國GDP的MOM小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['GDPC1']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['GDPC1']

        # 處理變數： 利用函數計算MOM增長
        self.process_variable = "percent_change_track_adjusted_values_change(GDPC1,windows = 30) < - 0.01"

    def rule_22(self):
        # 描述
        self.description = "動態美國GDP的MOM小於-5%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['GDPC1']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['GDPC1']

        # 處理變數： 利用函數計算MOM增長
        self.process_variable = "percent_change_track_adjusted_values_change(GDPC1,windows = 30) < - 0.05"

    def rule_23(self):
        # 描述
        self.description = "動態美國GDP的MOM小於-10%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['GDPC1']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['GDPC1']

        # 處理變數： 利用函數計算MOM增長
        self.process_variable = "percent_change_track_adjusted_values_change(GDPC1,windows = 30) < - 0.1"

    def rule_24(self):
        # 描述
        self.description = "靜態美國失業率的250天變動幅度大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數： 靜態失業率250天內的變化是否增加1%
        self.process_variable = "percent_change_record_daily_value_change(UNRATE,windows = 250) > 0.01"

    def rule_25(self):
        # 描述
        self.description = "靜態美國失業率的250天變動幅度大於50%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數： 靜態失業率250天內的變化是否增加5%
        self.process_variable = "percent_change_record_daily_value_change(UNRATE,windows = 250) > 0.5"

    def rule_26(self):
        # 描述
        self.description = "靜態美國失業率的250天變動幅度大於10%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數： 靜態失業率250天內的變化是否增加10%
        self.process_variable = "percent_change_record_daily_value_change(UNRATE,windows = 250) > 0.1"

    def rule_27(self):
        # 描述
        self.description = "靜態美國失業率的250天變動幅度小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數： 靜態失業率250天內的變化是否低於1%
        self.process_variable = "percent_change_record_daily_value_change(UNRATE,windows = 250) < - 0.01"

    def rule_28(self):
        # 描述
        self.description = "靜態美國失業率的250天變動幅度小於-5%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數： 靜態失業率250天內的變化是否低於5%
        self.process_variable = "percent_change_record_daily_value_change(UNRATE,windows = 250) < - 0.05"

    def rule_29(self):
        # 描述
        self.description = "靜態美國失業率的250天變動幅度小於-10%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數： 靜態失業率250天內的變化是否低於10%
        self.process_variable = "percent_change_record_daily_value_change(UNRATE,windows = 250) < - 0.1"

    def rule_30(self):
        # 描述
        self.description = "動態美國失業率的250天變動幅度大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數： 動態失業率250天內的變化是否增加1%
        self.process_variable = "percent_change_track_adjusted_values_change(UNRATE,windows = 250) > 0.01"

    def rule_31(self):
        # 描述
        self.description = "動態美國失業率的250天變動幅度大於10%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數： 動態美國失業率的250天變動幅度大於10
        self.process_variable = "percent_change_track_adjusted_values_change(UNRATE,windows = 250) > 0.1"

    def rule_32(self):
        # 描述
        self.description = "動態美國失業率的250天變動幅度大於10%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數： 動態美國失業率的250天變動幅度大於10
        self.process_variable = "percent_change_track_adjusted_values_change(UNRATE,windows = 250) > 0.1"

    def rule_33(self):
        # 描述
        self.description = "動態美國失業率的250天變動幅度小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數： 動態失業率250天內的變化是否低於1%
        self.process_variable = "percent_change_track_adjusted_values_change(UNRATE,windows = 250) < - 0.01"

    def rule_34(self):
        # 描述
        self.description = "動態美國失業率的250天變動幅度小於-50%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數： 動態失業率250天內的變化是否低於5%
        self.process_variable = "percent_change_track_adjusted_values_change(UNRATE,windows = 250) < - 0.5"

    def rule_35(self):
        # 描述
        self.description = "動態美國失業率的250天變動幅度小於-10%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數： 動態失業率250天內的變化是否低於10%
        self.process_variable = "percent_change_track_adjusted_values_change(UNRATE,windows = 250) < - 0.1"

    def rule_36(self):
        # 描述
        self.description = "靜態美國核心CPI的120天變動幅度大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數： 靜態美國核心CPI的120天變動幅度大於1%
        self.process_variable = "percent_change_record_daily_value_change(CPILFESL,windows = 120) > 0.01"

    def rule_37(self):
        # 描述
        self.description = "靜態美國核心CPI的120天變動幅度大於5%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數： 靜態美國核心CPI在120天內是否增長超過5%
        self.process_variable = "percent_change_record_daily_value_change(CPILFESL,windows = 120) > 0.05"

    def rule_38(self):
        # 描述
        self.description = "靜態美國核心CPI的120天變動幅度大於10%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數： 靜態美國核心CPI在120天內是否增長超過10%
        self.process_variable = "percent_change_record_daily_value_change(CPILFESL,windows = 120) > 0.1"

    def rule_39(self):
        # 描述
        self.description = "靜態美國核心CPI的120天變動幅度小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數： 靜態美國核心CPI在120天內是否低於超過1%
        self.process_variable = "percent_change_record_daily_value_change(CPILFESL,windows = 120) < - 0.01"
        
    def rule_40(self):
        # 描述
        self.description = "靜態美國核心CPI的120天變動幅度小於-50%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數： 靜態美國核心CPI在120天內是否低於超過5%
        self.process_variable = "percent_change_record_daily_value_change(CPILFESL,windows = 120) < - 0.5"

    def rule_41(self):
        # 描述
        self.description = "靜態美國核心CPI的120天變動幅度小於-10%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數： 靜態美國核心CPI在120天內是否低於超過10%
        self.process_variable = "percent_change_record_daily_value_change(CPILFESL,windows = 120) < - 0.1"


    def rule_42(self): 
        # 描述
        self.description = "動態美國核心CPI的120天變動幅度大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數： 動態美國核心CPI在120天內是否增長超過1%
        self.process_variable = "percent_change_track_adjusted_values_change(CPILFESL,windows = 120) > 0.01"

    def rule_43(self):
        # 描述
        self.description = "動態美國核心CPI的120天變動幅度大於5%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數： 動態美國核心CPI在120天內是否增長超過5%
        self.process_variable = "percent_change_track_adjusted_values_change(CPILFESL,windows = 120) > 0.05"

    def rule_44(self):
        # 描述
        self.description = "動態美國核心CPI的120天變動幅度大於10%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數： 動態美國核心CPI在120天內是否增長超過10%
        self.process_variable = "percent_change_track_adjusted_values_change(CPILFESL,windows = 120) > 0.1"

    def rule_45(self):
        # 描述
        self.description = "動態美國核心CPI的120天變動幅度小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數： 動態美國核心CPI在120天內是否低於超過1%
        self.process_variable = "percent_change_track_adjusted_values_change(CPILFESL,windows = 120) < - 0.01"

    def rule_46(self):
        # 描述
        self.description = "動態美國核心CPI的120天變動幅度小於-50%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數： 動態美國核心CPI在120天內是否低於超過5%
        self.process_variable = "percent_change_track_adjusted_values_change(CPILFESL,windows = 120) < - 0.5"

    def rule_47(self):
        # 描述
        self.description = "動態美國核心CPI的120天變動幅度小於-10%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數： 動態美國核心CPI在120天內是否低於超過10%
        self.process_variable = "percent_change_track_adjusted_values_change(CPILFESL,windows = 120) < - 0.1"

    def rule_48(self):
        # 描述
        self.description = "動態美國GDP的250天變動幅度大於1%且動態美國失業率的250天變動幅度小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['GDPC1', 'UNRATE']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['GDPC1', 'UNRATE']

        # 處理變數： 動態 GDP 比 250 天前增加 1%，且動態失業率比 250 天前低於 1%
        gdp_condition = "percent_change_track_adjusted_values_change(GDPC1, windows=250) > 0.01"
        unemployment_condition = "percent_change_track_adjusted_values_change(UNRATE, windows=250) < - 0.01"

        # 使用逐元素邏輯運算符來結合條件
        self.process_variable = f"({gdp_condition}) & ({unemployment_condition})"

    def rule_49(self):
        # 描述
        self.description = "靜態美國生產者物價指數的250天變動幅度高於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['PPIACO']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PPIACO']

        # 處理變數： 靜態工業生產數據比250天前增加1%
        self.process_variable = "percent_change_record_daily_value_change(PPIACO,windows = 250) > 0.01"

    def rule_50(self):
        # 描述
        self.description = "靜態美國生產者物價指數的250天變動幅度高於5%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['PPIACO']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PPIACO']

        # 處理變數： 靜態工業生產數據比250天前增加5%
        self.process_variable = "percent_change_record_daily_value_change(PPIACO,windows = 250) > 0.05"

    def rule_51(self):
        # 描述
        self.description = "靜態美國生產者物價指數的250天變動幅度高於10%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['PPIACO']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PPIACO']

        # 處理變數： 靜態工業生產數據比250天前增加10%
        self.process_variable = "percent_change_record_daily_value_change(PPIACO,windows = 250) > 0.1"

    def rule_52(self):
        # 描述
        self.description = "靜態美國生產者物價指數的250天變動幅度低於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['PPIACO']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PPIACO']

        # 處理變數： 靜態工業生產數據比250天前低於1%
        self.process_variable = "percent_change_record_daily_value_change(PPIACO,windows = 250) < - 0.01"

    def rule_53(self):
        # 描述
        self.description = "靜態美國生產者物價指數的250天變動幅度低於-5%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['PPIACO']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PPIACO']

        # 處理變數： 靜態工業生產數據比250天前低於5%
        self.process_variable = "percent_change_record_daily_value_change(PPIACO,windows = 250) < - 0.05"

    def rule_54(self):
        # 描述
        self.description = "靜態美國生產者物價指數的250天變動幅度低於-10%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['PPIACO']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PPIACO']

        # 處理變數： 靜態工業生產數據比250天前低於10%
        self.process_variable = "percent_change_record_daily_value_change(PPIACO,windows = 250) < - 0.1"

    def rule_55(self):
        # 描述
        self.description = "動態美國生產者物價指數的250天變動幅度大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['PPIACO']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PPIACO']

        # 處理變數： 工業生產數據250天前增加1%
        self.process_variable = "percent_change_track_adjusted_values_change(PPIACO,windows = 250) > 0.01"

    def rule_56(self):
        # 描述
        self.description = "動態美國生產者物價指數的250天變動幅度大於2%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['PPIACO']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PPIACO']

        # 處理變數： 動態工業生產數據250天前增加2%
        self.process_variable = "percent_change_track_adjusted_values_change(PPIACO,windows = 250) > 0.02"

    def rule_57(self):
        # 描述
        self.description = "動態美國生產者物價指數的250天變動幅度大於5%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['PPIACO']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PPIACO']

        # 處理變數： 動態工業生產數據250天前增加5%
        self.process_variable = "percent_change_track_adjusted_values_change(PPIACO,windows = 250) > 0.05"

    def rule_58(self):
        # 描述
        self.description = "動態美國生產者物價指數的250天變動幅度大於10%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['PPIACO']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PPIACO']

        # 處理變數： 動態工業生產數據250天前增加10%
        self.process_variable = "percent_change_track_adjusted_values_change(PPIACO,windows = 250) > 0.1"

    def rule_59(self):
        # 描述
        self.description = "動態美國生產者物價指數的250天變動幅度小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['PPIACO']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PPIACO']

        # 處理變數： 工業生產數據250天前低於1%
        self.process_variable = "percent_change_track_adjusted_values_change(PPIACO,windows = 250) < - 0.01"

    def rule_60(self):
        # 描述
        self.description = "動態美國生產者物價指數的250天變動幅度小於-5%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['PPIACO']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PPIACO']

        # 處理變數： 動態工業生產數據250天前低於5%
        self.process_variable = "percent_change_track_adjusted_values_change(PPIACO,windows = 250) < - 0.05"

    def rule_61(self):
        # 描述
        self.description = "動態美國生產者物價指數的250天變動幅度小於-10%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['PPIACO']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PPIACO']

        # 處理變數： 動態工業生產數據250天前低於10%
        self.process_variable = "percent_change_track_adjusted_values_change(PPIACO,windows = 250) < - 0.1"

    def rule_62(self):
        # 描述
        self.description = "靜態美國30年期固定利率抵押貸款平均值的30天變動幅高於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['MORTGAGE30US']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['MORTGAGE30US']

        # 處理變數： 靜態房屋價格指數30天增加1%
        self.process_variable = "percent_change_record_daily_value_change(MORTGAGE30US, windows=30) > 0.01"

    def rule_63(self):
        # 描述
        self.description = "靜態美國30年期固定利率抵押貸款平均值的30天變動幅高於5%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['MORTGAGE30US']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['MORTGAGE30US']

        # 處理變數： 靜態房屋價格指數30天增加5%
        self.process_variable = "percent_change_record_daily_value_change(MORTGAGE30US, windows=30) > 0.05"
    
    def rule_64(self):
        # 描述
        self.description = "靜態美國30年期固定利率抵押貸款平均值的30天變動幅高於10%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['MORTGAGE30US']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['MORTGAGE30US']

        # 處理變數： 靜態房屋價格指數30天增加10%
        self.process_variable = "percent_change_record_daily_value_change(MORTGAGE30US, windows=30) > 0.1"

    def rule_65(self):
        # 描述
        self.description = "靜態美國30年期固定利率抵押貸款平均值的250天變動幅高於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['MORTGAGE30US']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['MORTGAGE30US']

        # 處理變數： 靜態房屋價格指數250天增加1%
        self.process_variable = "percent_change_record_daily_value_change(MORTGAGE30US, windows=250) > 0.01"

    def rule_66(self):
        # 描述
        self.description = "靜態美國30年期固定利率抵押貸款平均值的250天變動幅高於5%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['MORTGAGE30US']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['MORTGAGE30US']

        # 處理變數： 靜態房屋價格指數250天增加5%
        self.process_variable = "percent_change_record_daily_value_change(MORTGAGE30US, windows=250) > 0.05"
    
    def rule_67(self):
        # 描述
        self.description = "靜態美國30年期固定利率抵押貸款平均值的250天變動幅高於10%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['MORTGAGE30US']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['MORTGAGE30US']

        # 處理變數： 靜態房屋價格指數250內增加10%
        self.process_variable = "percent_change_record_daily_value_change(MORTGAGE30US, windows=250) > 0.1"

    def rule_68(self):
        # 描述
        self.description = "靜態美國30年期固定利率抵押貸款平均值的30天變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['MORTGAGE30US']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['MORTGAGE30US']

        # 處理變數： 靜態房屋價格指數30天低於1%
        self.process_variable = "percent_change_record_daily_value_change(MORTGAGE30US, windows=30) < - 0.01"

    def rule_69(self):
        # 描述
        self.description = "靜態美國30年期固定利率抵押貸款平均值的30天變動幅小於-5%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['MORTGAGE30US']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['MORTGAGE30US']

        # 處理變數： 靜態房屋價格指數30天低於5%
        self.process_variable = "percent_change_record_daily_value_change(MORTGAGE30US, windows=30) < - 0.05"
    
    def rule_70(self):
        # 描述
        self.description = "靜態美國30年期固定利率抵押貸款平均值的30天變動幅小於-10%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['MORTGAGE30US']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['MORTGAGE30US']

        # 處理變數： 靜態房屋價格指數30天低於10%
        self.process_variable = "percent_change_record_daily_value_change(MORTGAGE30US, windows=30) < - 0.1"

    def rule_71(self):
        # 描述
        self.description = "靜態美國30年期固定利率抵押貸款平均值的250天變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['MORTGAGE30US']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['MORTGAGE30US']

        # 處理變數： 靜態房屋價格指數250天低於1%
        self.process_variable = "percent_change_record_daily_value_change(MORTGAGE30US, windows=250) < - 0.01"

    def rule_72(self):
        # 描述
        self.description = "靜態美國30年期固定利率抵押貸款平均值的250天變動幅小於-5%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['MORTGAGE30US']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['MORTGAGE30US']

        # 處理變數： 靜態房屋價格指數250天低於5%
        self.process_variable = "percent_change_record_daily_value_change(MORTGAGE30US, windows=250) < - 0.05"
    
    def rule_73(self):
        # 描述
        self.description = "靜態美國30年期固定利率抵押貸款平均值的250天變動幅小於-10%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['MORTGAGE30US']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['MORTGAGE30US']

        # 處理變數： 靜態房屋價格指數250低於10%
        self.process_variable = "percent_change_record_daily_value_change(MORTGAGE30US, windows=250) < - 0.1"

    def rule_74(self): 
        # 描述
        self.description = "動態美國30年期固定利率抵押貸款平均值的30天變動幅度大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['MORTGAGE30US']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['MORTGAGE30US']

        # 處理變數： 動態房屋價格指數30天增加1%
        self.process_variable = "percent_change_track_adjusted_values_change(MORTGAGE30US, windows=30) > 0.01"

    def rule_75(self):
        # 描述
        self.description = "動態美國30年期固定利率抵押貸款平均值的30天變動幅度大於5%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['MORTGAGE30US']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['MORTGAGE30US']

        # 處理變數： 動態房屋價格指數30天增加5%
        self.process_variable = "percent_change_track_adjusted_values_change(MORTGAGE30US, windows=30) > 0.05"
    
    def rule_76(self):
        # 描述
        self.description = "動態美國30年期固定利率抵押貸款平均值的30天變動幅度大於10%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['MORTGAGE30US']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['MORTGAGE30US']

        # 處理變數： 動態房屋價格指數30天增加10%
        self.process_variable = "percent_change_track_adjusted_values_change(MORTGAGE30US, windows=30) > 0.1"

    def rule_77(self):
        # 描述
        self.description = "動態美國30年期固定利率抵押貸款平均值的250天變動幅度大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['MORTGAGE30US']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['MORTGAGE30US']

        # 處理變數： 動態房屋價格指數250天增加1%
        self.process_variable = "percent_change_track_adjusted_values_change(MORTGAGE30US, windows=250) > 0.01"

    def rule_78(self):
        # 描述
        self.description = "動態美國30年期固定利率抵押貸款平均值的250天變動幅度大於5%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['MORTGAGE30US']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['MORTGAGE30US']

        # 處理變數： 動態房屋價格指數250天增加5%
        self.process_variable = "percent_change_track_adjusted_values_change(MORTGAGE30US, windows=250) > 0.05"
    
    def rule_79(self):
        # 描述
        self.description = "動態美國30年期固定利率抵押貸款平均值的250天變動幅度大於10%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['MORTGAGE30US']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['MORTGAGE30US']

        # 處理變數： 動態房屋價格指數250內增加10%
        self.process_variable = "percent_change_track_adjusted_values_change(MORTGAGE30US, windows=250) > 0.1"

    def rule_80(self): 
        # 描述
        self.description = "動態美國30年期固定利率抵押貸款平均值的30天變動幅度小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['MORTGAGE30US']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['MORTGAGE30US']

        # 處理變數： 動態房屋價格指數30天低於1%
        self.process_variable = "percent_change_track_adjusted_values_change(MORTGAGE30US, windows=30) < - 0.01"

    def rule_81(self):
        # 描述
        self.description = "動態美國30年期固定利率抵押貸款平均值的30天變動幅度小於-5%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['MORTGAGE30US']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['MORTGAGE30US']

        # 處理變數： 動態房屋價格指數30天低於5%
        self.process_variable = "percent_change_track_adjusted_values_change(MORTGAGE30US, windows=30) < - 0.05"
    
    def rule_82(self):
        # 描述
        self.description = "動態美國30年期固定利率抵押貸款平均值的30天變動幅度小於-10%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['MORTGAGE30US']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['MORTGAGE30US']

        # 處理變數： 動態房屋價格指數30天低於10%
        self.process_variable = "percent_change_track_adjusted_values_change(MORTGAGE30US, windows=30) < - 0.1"

    def rule_83(self):
        # 描述
        self.description = "動態美國30年期固定利率抵押貸款平均值的250天變動幅度小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['MORTGAGE30US']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['MORTGAGE30US']

        # 處理變數： 動態房屋價格指數250天低於1%
        self.process_variable = "percent_change_track_adjusted_values_change(MORTGAGE30US, windows=250) < - 0.01"

    def rule_84(self):
        # 描述
        self.description = "動態美國30年期固定利率抵押貸款平均值的250天變動幅度小於-5%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['MORTGAGE30US']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['MORTGAGE30US']

        # 處理變數： 動態房屋價格指數250天低於5%
        self.process_variable = "percent_change_track_adjusted_values_change(MORTGAGE30US, windows=250) < - 0.05"
    
    def rule_85(self):
        # 描述
        self.description = "動態美國30年期固定利率抵押貸款平均值的250天變動幅度小於-10%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['MORTGAGE30US']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['MORTGAGE30US']

        # 處理變數： 動態房屋價格指數250低於10%
        self.process_variable = "percent_change_track_adjusted_values_change(MORTGAGE30US, windows=250) < - 0.1"

    def rule_86(self): 
        # 描述
        self.description = "靜態美國消費者信心指數的250天變動幅高於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['UMCSENT']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UMCSENT']

        # 處理變數： 靜態消費者信心指數250天增加1%
        self.process_variable = "percent_change_record_daily_value_change(UMCSENT, windows=250) > 0.01"

    def rule_87(self):
        # 描述
        self.description = "靜態美國消費者信心指數的250天變動幅高於5%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['UMCSENT']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UMCSENT']

        # 處理變數： 靜態消費者信心指數250天增加5%
        self.process_variable = "percent_change_record_daily_value_change(UMCSENT, windows=250) > 0.05"

    def rule_88(self):
        # 描述
        self.description = "靜態美國消費者信心指數的250天變動幅高於10%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['UMCSENT']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UMCSENT']

        # 處理變數： 靜態消費者信心指數250天增加10%
        self.process_variable = "percent_change_record_daily_value_change(UMCSENT, windows=250) > 0.1"

    def rule_89(self):
        # 描述
        self.description = "靜態美國消費者信心指數的250天變動幅低於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['UMCSENT']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UMCSENT']

        # 處理變數： 靜態消費者信心指數250天低於1%
        self.process_variable = "percent_change_record_daily_value_change(UMCSENT, windows=250) < - 0.01"

    def rule_90(self):
        # 描述
        self.description = "靜態美國消費者信心指數的250天變動幅低於-5%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['UMCSENT']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UMCSENT']

        # 處理變數： 靜態消費者信心指數250天低於5%
        self.process_variable = "percent_change_record_daily_value_change(UMCSENT, windows=250) < - 0.05"

    def rule_91(self):
        # 描述
        self.description = "靜態美國消費者信心指數的250天變動幅低於-10%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['UMCSENT']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UMCSENT']

        # 處理變數： 靜態消費者信心指數250天低於10%
        self.process_variable = "percent_change_record_daily_value_change(UMCSENT, windows=250) < - 0.1"

    def rule_92(self):
        # 描述
        self.description = "動態美國消費者信心指數的250天變動幅度大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['UMCSENT']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UMCSENT']

        # 處理變數： 動態消費者信心指數250天增加1%
        self.process_variable = "percent_change_track_adjusted_values_change(UMCSENT, windows=250) > 0.01"

    def rule_93(self):
        # 描述
        self.description = "動態美國消費者信心指數的250天變動幅度大於5%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['UMCSENT']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UMCSENT']

        # 處理變數： 動態消費者信心指數250天增加5%
        self.process_variable = "percent_change_track_adjusted_values_change(UMCSENT, windows=250) > 0.05"

    def rule_94(self):
        # 描述
        self.description = "動態美國消費者信心指數的250天變動幅度大於10%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['UMCSENT']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UMCSENT']

        # 處理變數： 動態消費者信心指數250天增加10%
        self.process_variable = "percent_change_track_adjusted_values_change(UMCSENT, windows=250) > 0.1"

    def rule_95(self):
        # 描述
        self.description = "動態美國消費者信心指數的250天變動幅度小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['UMCSENT']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UMCSENT']

        # 處理變數： 動態消費者信心指數250天低於1%
        self.process_variable = "percent_change_track_adjusted_values_change(UMCSENT, windows=250) < - 0.01"

    def rule_96(self):
        # 描述
        self.description = "動態美國消費者信心指數的250天變動幅度小於-5%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['UMCSENT']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UMCSENT']

        # 處理變數： 動態消費者信心指數250天低於5%
        self.process_variable = "percent_change_track_adjusted_values_change(UMCSENT, windows=250) < - 0.05"

    def rule_97(self):
        # 描述
        self.description = "動態美國消費者信心指數的250天變動幅度小於-10%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['UMCSENT']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UMCSENT']

        # 處理變數： 動態消費者信心指數250天低於10%
        self.process_variable = "percent_change_track_adjusted_values_change(UMCSENT, windows=250) < - 0.1"

    def rule_98(self):
        # 描述
        self.description = "靜態美國非農就業人數的250天變動幅大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數： 靜態非農就業數據250天增加1%
        self.process_variable = "percent_change_record_daily_value_change(PAYEMS, windows=250) > 0.01"

    def rule_99(self):
        # 描述
        self.description = "靜態美國非農就業人數的250天變動幅大於5%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數： 靜態非農就業數據250天增加5%
        self.process_variable = "percent_change_record_daily_value_change(PAYEMS, windows=250) > 0.05"

    def rule_100(self):
        # 描述
        self.description = "靜態美國非農就業人數的250天變動幅大於10%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數： 靜態非農就業數據250天增加10%
        self.process_variable = "percent_change_record_daily_value_change(PAYEMS, windows=250) > 0.1"

    def rule_101(self):
        # 描述
        self.description = "靜態美國非農就業人數的250天變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數： 靜態非農就業數據250天低於1%
        self.process_variable = "percent_change_record_daily_value_change(PAYEMS, windows=250) < - 0.01"

    def rule_102(self):
        # 描述
        self.description = "靜態美國非農就業人數的250天變動幅小於-5%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數： 靜態非農就業數據250天低於5%
        self.process_variable = "percent_change_record_daily_value_change(PAYEMS, windows=250) < - 0.05"

    def rule_103(self):
        # 描述
        self.description = "靜態美國非農就業人數的250天變動幅小於-10%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數： 靜態非農就業數據250天低於10%
        self.process_variable = "percent_change_record_daily_value_change(PAYEMS, windows=250) < - 0.1"

    def rule_104(self):
        # 描述
        self.description = "動態美國非農就業人數的250天變動幅度大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數： 動態非農就業數據250天增加1%
        self.process_variable = "percent_change_track_adjusted_values_change(PAYEMS, windows=250) > 0.01"

    def rule_105(self):
        # 描述
        self.description = "動態美國非農就業人數的250天變動幅度大於5%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數： 動態非農就業數據250天增加5%
        self.process_variable = "percent_change_track_adjusted_values_change(PAYEMS, windows=250) > 0.05"

    def rule_106(self):
        # 描述
        self.description = "動態美國非農就業人數的250天變動幅度大於10%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數： 動態非農就業數據250天增加10%
        self.process_variable = "percent_change_track_adjusted_values_change(PAYEMS, windows=250) > 0.1"

    def rule_107(self):
        # 描述
        self.description = "動態美國非農就業人數的250天變動幅度小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數： 動態非農就業數據250天低於1%
        self.process_variable = "percent_change_track_adjusted_values_change(PAYEMS, windows=250) < - 0.01"

    def rule_108(self):
        # 描述
        self.description = "動態美國非農就業人數的250天變動幅度小於-5%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數： 動態非農就業數據250天低於5%
        self.process_variable = "percent_change_track_adjusted_values_change(PAYEMS, windows=250) < - 0.05"

    def rule_109(self):
        # 描述
        self.description = "動態美國非農就業人數的250天變動幅度小於-1000%"

        # 資料庫的欄位名稱
        self.use_data = ['']

        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']

        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數： 動態非農就業數據250天低於1000%
        self.process_variable = "percent_change_track_adjusted_values_change(PAYEMS, windows=250) < - 100"

    def rule_110(self):
        # 描述
        self.description = "靜態美國非農就業人數比250天前增加"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數
        self.process_variable = "diff_record_daily_value_change(PAYEMS,windows = 250) >  0 "

    def rule_111(self):
        # 描述
        self.description = "靜態美國非農就業人數比250天前減少"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數
        self.process_variable = "diff_record_daily_value_change(PAYEMS,windows = 250) < -  0 "

    def rule_112(self):
        # 描述
        self.description = "動態美國非農就業人數比250天前增加"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數
        self.process_variable = "diff_track_adjusted_values_change(PAYEMS,windows = 250) >  0 "

    def rule_113(self):
        # 描述
        self.description = "動態美國非農就業人數比250天前減少"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數
        self.process_variable = "diff_track_adjusted_values_change(PAYEMS,windows = 250) < -  0 "

    def rule_114(self):
        # 描述
        self.description = "靜態美國M2比250天前減少"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['WM2NS']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['WM2NS']

        # 處理變數
        self.process_variable = "diff_record_daily_value_change(WM2NS,windows = 250) < -  0 "
    
    def rule_115(self):
        # 描述
        self.description = "靜態美國M2比250天前增加"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['WM2NS']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['WM2NS']

        # 處理變數
        self.process_variable = "diff_record_daily_value_change(WM2NS,windows = 250) > 0  "
    
    def rule_116(self):
        # 描述
        self.description = "動態美國M2比60天前減少"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['WM2NS']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['WM2NS']

        # 處理變數
        self.process_variable = "diff_track_adjusted_values_change(WM2NS,windows = 60) < - 0 "
    
    def rule_117(self):
        # 描述
        self.description = "動態美國M2比250天前增加"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['WM2NS']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['WM2NS']

        # 處理變數
        self.process_variable = "diff_track_adjusted_values_change(WM2NS,windows = 250) > 0  "

    def rule_118(self):
        # 描述
        self.description = "靜態美國工業生產指數的250天變動幅大於0%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['INDPRO']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['INDPRO']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(INDPRO,windows = 250) >  0 "

    def rule_119(self):
        # 描述
        self.description = "動態美國工業生產指數的250天變動幅小於0%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['INDPRO']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['INDPRO']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(INDPRO,windows = 250) < -  0 "

    def rule_120(self):
        # 描述
        self.description = "靜態美國10年期固定期限美國公債市場報酬率的250天變動幅大於0"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['DGS10']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['DGS10']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(DGS10,windows = 250) >  0 "

    def rule_121(self): 
        # 描述
        self.description = "動態10年期固定期限美國公債市場報酬率的250天變動幅小於0"
        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['DGS10']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['DGS10']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(DGS10,windows = 250) <   0 "

    def rule_122(self):
        # 描述
        self.description = "靜態態美國銀行隔夜融資量比250天前增加"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['OBFRVOL']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['OBFRVOL']

        # 處理變數
        self.process_variable = "diff_record_daily_value_change(OBFRVOL,windows = 250) >  0 "

    def rule_123(self):
        # 描述
        self.description = "動態美國銀行隔夜融資量比250天前增加"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['OBFRVOL']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['OBFRVOL']

        # 處理變數
        self.process_variable = "diff_track_adjusted_values_change(OBFRVOL,windows = 250) < -  0 "

    def rule_124(self):
        # 描述
        self.description = "靜態態美國GDP比250天前減少"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['GDPC1']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['GDPC1']

        # 處理變數
        self.process_variable = "diff_record_daily_value_change(GDPC1,windows = 250) <  0 "
    
    def rule_125(self):
        # 描述
        self.description = "靜態態美國GDP比250天前增加"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['GDPC1']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['GDPC1']

        # 處理變數
        self.process_variable = "diff_record_daily_value_change(GDPC1,windows = 250) > 0  "
    
    def rule_126(self):
        # 描述
        self.description = "動態美國GDP比250天前減少"
        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['GDPC1']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['GDPC1']

        # 處理變數
        self.process_variable = "diff_track_adjusted_values_change(GDPC1,windows = 250) <  0 "
    
    def rule_127(self):
        # 描述
        self.description = "動態美國GDP比250天前增加"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['GDPC1']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['GDPC1']

        # 處理變數
        self.process_variable = "diff_track_adjusted_values_change(GDPC1,windows = 250) > 0  "
    
    def rule_128(self):
        # 描述
        self.description = "動態美國GDP的250天變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['GDPC1']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['GDPC1']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(GDPC1,windows = 250) < -0.01 "
                
    def rule_129(self):
        # 描述
        self.description = "靜態美國GDP的250天變動幅大於1%"
        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['GDPC1']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['GDPC1']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(GDPC1,windows = 250) > 0.01 "
      
    def rule_130(self):
        # 描述
        self.description = "動態美國失業率的250天變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(UNRATE, windows = 250) < -0.01"
    
    def rule_131(self):
        # 描述
        self.description = "動態美國失業率的250天變動幅大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(UNRATE, windows = 250) > 0.01"

    def rule_132(self):
        # 描述
        self.description = "動態美國失業率的250天變動幅小於-2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(UNRATE, windows = 250) < -0.02"

    def rule_133(self):
        # 描述
        self.description = "動態美國失業率的250天變動幅大於2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(UNRATE, windows = 250) > 0.02"

    def rule_134(self):
        # 描述
        self.description = "動態美國失業率的250天變動幅小於-3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(UNRATE, windows = 250) < -0.03"

    def rule_135(self):
        # 描述
        self.description = "動態美國失業率的250天變動幅大於3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(UNRATE, windows = 250) > 0.03"

    def rule_136(self):
        # 描述
        self.description = "動態美國失業率的250天變動幅小於-4%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(UNRATE, windows = 250) < -0.04"

    def rule_137(self):
        # 描述
        self.description = "動態美國失業率的250天變動幅大於4%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(UNRATE, windows = 250) > 0.04"

    def rule_138(self):
        # 描述
        self.description = "動態美國失業率的250天變動幅小於-5%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(UNRATE, windows = 250) < -0.05"

    def rule_139(self):
        # 描述
        self.description = "動態美國失業率的250天變動幅大於5%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(UNRATE, windows = 250) > 0.05"

    def rule_140(self):
        # 描述
        self.description = "動態美國失業率的250天變動幅小於-6%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(UNRATE, windows = 250) < -0.06"

    def rule_141(self):
        # 描述
        self.description = "動態美國失業率的250天變動幅大於6%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(UNRATE, windows = 250) > 0.06"

    def rule_142(self):
        # 描述
        self.description = "動態美國失業率的250天變動幅小於-7%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(UNRATE, windows = 250) < -0.07"

    def rule_143(self):
        # 描述
        self.description = "動態美國失業率的250天變動幅大於7%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(UNRATE, windows = 250) > 0.07"

    def rule_144(self):
        # 描述
        self.description = "靜態美國失業率的250天變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(UNRATE, windows = 250) < -0.01"

    def rule_145(self):
        # 描述
        self.description = "靜態美國失業率的250天變動幅大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(UNRATE, windows = 250) > 0.01"


    def rule_146(self):
        # 描述
        self.description = "靜態美國失業率的250天變動幅小於-2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(UNRATE, windows = 250) < -0.02"

    def rule_147(self):
        # 描述
        self.description = "靜態美國失業率的250天變動幅大於2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(UNRATE, windows = 250) > 0.02"

    def rule_148(self):
        # 描述
        self.description = "靜態美國失業率的250天變動幅小於-3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(UNRATE, windows = 250) < -0.03"

    
    def rule_149(self):
        # 描述
        self.description = "靜態美國失業率的250天變動幅大於3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(UNRATE, windows = 250) > 0.03"
    
    def rule_150(self):
        # 描述
        self.description = "靜態美國失業率的250天變動幅小於-4%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(UNRATE, windows = 250) < -0.04"

    def rule_151(self):
        # 描述
        self.description = "靜態美國失業率的250天變動幅大於4%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(UNRATE, windows = 250) > 0.04"

    def rule_152(self):
        # 描述
        self.description = "靜態美國失業率的250天變動幅小於-5%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(UNRATE, windows = 250) < -0.05"
    
    def rule_153(self):
        # 描述
        self.description = "靜態美國失業率的250天變動幅大於5%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(UNRATE, windows = 250) > 0.05"

    def rule_154(self):
        # 描述
        self.description = "靜態美國失業率的250天變動幅小於-6%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(UNRATE, windows = 250) < -0.06"

    
    def rule_155(self):
        # 描述
        self.description = "靜態美國失業率的250天變動幅大於6%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(UNRATE, windows = 250) > 0.06"

    def rule_156(self):
        # 描述
        self.description = "靜態美國失業率的250天變動幅小於-7%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(UNRATE, windows = 250) < -0.07"

    def rule_157(self):
        # 描述
        self.description = "靜態美國失業率的250天變動幅大於7%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['UNRATE']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['UNRATE']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(UNRATE, windows = 250) > 0.07"

    def rule_158(self):
        # 描述
        self.description = "靜態隔夜逆回購的500天變動幅小於-5%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['RRPONTSYD']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['RRPONTSYD']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(RRPONTSYD, windows = 500) < -0.05"

    def rule_159(self):
        # 描述
        self.description = "靜態隔夜逆回購的500天變動幅大於5%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['RRPONTSYD']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['RRPONTSYD']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(RRPONTSYD, windows = 500) > 0.05"
    
    def rule_160(self):
        # 描述
        self.description = "動態隔夜逆回購的500天變動幅大於5%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['RRPONTSYD']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['RRPONTSYD']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(RRPONTSYD, windows = 500) > 0.05"


    def rule_161(self):
         # 描述
        self.description = "動態隔夜逆回購的500天變動幅小於5%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['RRPONTSYD']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['RRPONTSYD']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(RRPONTSYD, windows = 500) < 0.05"
    
    def rule_162(self):
         # 描述
        self.description = "動態隔夜逆回購的500天變動幅大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['RRPONTSYD']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['RRPONTSYD']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(RRPONTSYD, windows = 500) > 0.01"
    
    def rule_163(self):
        # 描述
        self.description = "動態隔夜逆回購的500天變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['RRPONTSYD']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['RRPONTSYD']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(RRPONTSYD, windows = 500) < -0.01"
    
    def rule_164(self):
        # 描述
        self.description = "靜態隔夜逆回購的500天變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['RRPONTSYD']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['RRPONTSYD']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(RRPONTSYD, windows = 500) < -0.01"

    def rule_165(self):
         # 描述
        self.description = "靜態隔夜逆回購的500天變動幅大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['RRPONTSYD']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['RRPONTSYD']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(RRPONTSYD, windows = 500) > 0.01"        
    
    def rule_166(self):
        # 描述
        self.description = "動態隔夜逆回購的10天變動幅大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['RRPONTSYD']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['RRPONTSYD']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(RRPONTSYD, windows = 10) > 0.01"
    
    def rule_167(self):
        # 描述
        self.description = "動態隔夜逆回購的10天變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['RRPONTSYD']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['RRPONTSYD']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(RRPONTSYD, windows = 10) < -0.01"
    
    def rule_168(self):
        # 描述
        self.description = "靜態隔夜逆回購的10天變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['RRPONTSYD']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['RRPONTSYD']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(RRPONTSYD, windows = 10) < -0.01"

    def rule_169(self):
        # 描述
        self.description = "靜態隔夜逆回購的120天變動幅大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['RRPONTSYD']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['RRPONTSYD']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(RRPONTSYD, windows = 120) > 0.01"
    
    def rule_170(self):
        # 描述
        self.description = "動態準備金利率的120天變動幅大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['IORB']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['IORB']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(IORB, windows = 120) > 0.01"
    
    def rule_171(self):
        # 描述
        self.description = "動態準備金利率的120天變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['IORB']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['IORB']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(IORB, windows = 120) < -0.01"
    
    def rule_172(self):
        # 描述
        self.description = "靜態準備金利率的120天變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['IORB']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['IORB']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(IORB, windows = 120) < -0.01"

    def rule_173(self):
        # 描述
        self.description = "靜態準備金利率的120天變動幅大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['IORB']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['IORB']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(IORB, windows = 120) > 0.01"     

    def rule_174(self):
        # 描述
        self.description = "動態準備金利率的120天變動幅大於2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['IORB']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['IORB']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(IORB, windows = 120) > 0.02"
    
    def rule_175(self):
         # 描述
        self.description = "動態準備金利率的120天變動幅小於-2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['IORB']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['IORB']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(IORB, windows = 120) < -0.02"
    
    def rule_176(self):
        # 描述
        self.description = "靜態準備金利率的120天變動幅小於-2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['IORB']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['IORB']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(IORB, windows = 120) < -0.02"
        
    def rule_177(self):
         # 描述
        self.description = "靜態準備金利率的120天變動幅大於2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['IORB']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['IORB']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(IORB, windows = 120) > 0.02"    
         
    def rule_178(self):
        # 描述
        self.description = "動態準備金利率的120天變動幅大於3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['IORB']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['IORB']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(IORB, windows = 120) > 0.03"
    
    def rule_179(self):
        # 描述
        self.description = "動態準備金利率的120天變動幅小於-3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['IORB']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['IORB']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(IORB, windows = 120) < -0.03"
    
    def rule_180(self):
        # 描述
        self.description = "靜態準備金利率的120天變動幅小於-3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['IORB']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['IORB']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(IORB, windows = 120) < -0.03"
    
    def rule_181(self):
        # 描述
        self.description = "靜態準備金利率的120天變動幅大於3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['IORB']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['IORB']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(IORB, windows = 120) > 0.03"   
    
    def rule_182(self):
        # 描述
        self.description = "動態準備金利率的120天變動幅大於4%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['IORB']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['IORB']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(IORB, windows = 120) > 0.04"
    
    def rule_183(self):
        # 描述
        self.description = "動態準備金利率的120天變動幅小於-4%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['IORB']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['IORB']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(IORB, windows = 120) < -0.04"
    
    def rule_184(self):
        # 描述
        self.description = "靜態準備金利率的120天變動幅小於-4%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['IORB']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['IORB']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(IORB, windows = 120) < -0.04"

    def rule_185(self):
        # 描述
        self.description = "靜態準備金利率的120天變動幅大於4%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['IORB']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['IORB']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(IORB, windows = 120) > 0.04"   

    def rule_186(self):
         # 描述
        self.description = "動態準備金利率的120天變動幅大於5%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['IORB']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['IORB']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(IORB, windows = 120) > 0.05"
    
    def rule_187(self):
        # 描述
        self.description = "動態準備金利率的120天變動幅小於-5%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['IORB']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['IORB']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(IORB, windows = 120) < -0.05"
        
    def rule_188(self):
        # 描述
        self.description = "靜態準備金利率的120天變動幅小於-5%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['IORB']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['IORB']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(IORB, windows = 120) < -0.05"

    def rule_189(self):
        # 描述
        self.description = "靜態準備金利率的120天變動幅大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['IORB']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['IORB']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(IORB, windows = 240) > 0.01"   
    
    def rule_190(self):
        # 描述
        self.description = "動態準備金利率的240天變動幅大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['IORB']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['IORB']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(IORB, windows = 240) > 0.01"
    
    def rule_191(self):
        # 描述
        self.description = "動態準備金利率的240天變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['IORB']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['IORB']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(IORB, windows = 240) < -0.01"

    def rule_192(self):
        # 描述
        self.description = "靜態準備金利率的240天變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['IORB']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['IORB']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(IORB, windows = 240) < -0.01"

    def rule_193(self):
        # 描述
        self.description = "靜態準備金利率的240天變動幅高於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['IORB']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['IORB']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(IORB, windows = 240) > 0.01"   
    
    def rule_194(self):
         # 描述
        self.description = "動態產能利用率的240天變動幅大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(TCU, windows = 240) > 0.01"
    
    def rule_195(self):
        # 描述
        self.description = "動態產能利用率的240天變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(TCU, windows = 240) < -0.01"

    def rule_196(self):
        # 描述
        self.description = "靜態產能利用率的240天變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(TCU, windows = 240) < -0.01"
    
    def rule_197(self):
        # 描述
        self.description = "靜態產能利用率的240天變動幅大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(TCU, windows = 240) > 0.01"   

    def rule_198(self):
        # 描述
        self.description = "動態產能利用率的240天變動幅大於2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(TCU, windows = 240) > 0.02"
    
    def rule_199(self):
        # 描述
        self.description = "動態產能利用率的240天變動幅小於-2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(TCU, windows = 240) < -0.02"

    def rule_200(self):
        # 描述
        self.description = "靜態產能利用率的240天變動幅小於-2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(TCU, windows = 240) < -0.02"
    
    def rule_201(self):
        # 描述
        self.description = "靜態產能利用率的240天變動幅大於2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(TCU, windows = 240) > 0.02"   
    
    def rule_202(self):
        # 描述
        self.description = "動態產能利用率的240天變動幅大於3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(TCU, windows = 240) > 0.03"
    
    def rule_203(self):
        # 描述
        self.description = "動態產能利用率的240天變動幅小於-3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(TCU, windows = 240) < -0.03"

    def rule_204(self):
        # 描述
        self.description = "靜態產能利用率的240天變動幅小於-3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(TCU, windows = 240) < -0.03"

    def rule_205(self):
        # 描述
        self.description = "靜態產能利用率的240天變動幅大於3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(TCU, windows = 240) > 0.03"   

    def rule_206(self):
        # 描述
        self.description = "動態產能利用率的120天變動幅大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(TCU, windows = 120) > 0.01"
    
    def rule_207(self):
        # 描述
        self.description = "動態產能利用率的120天變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(TCU, windows = 120) < -0.01"

    def rule_208(self):
        # 描述
        self.description = "靜態產能利用率的120天變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(TCU, windows = 120) < -0.01"

    def rule_209(self):
        # 描述
        self.description = "靜態產能利用率的120天變動幅大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(TCU, windows = 120) > 0.01"   

    def rule_210(self):
         # 描述
        self.description = "動態產能利用率的120天變動幅大於2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(TCU, windows = 120) > 0.02"
    
    def rule_211(self):
        # 描述
        self.description = "動態產能利用率的120天變動幅小於-2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(TCU, windows = 120) < -0.02"

    def rule_212(self):
        # 描述
        self.description = "靜態產能利用率的120天變動幅小於-2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(TCU, windows = 120) < -0.02"

    def rule_213(self):
        # 描述
        self.description = "靜態產能利用率的120天變動幅大於2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(TCU, windows = 120) > 0.02"   

    def rule_214(self):
        # 描述
        self.description = "動態產能利用率的120天變動幅大於3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(TCU, windows = 120) > 0.03"
    
    
    def rule_215(self):
        # 描述
        self.description = "動態產能利用率的120天變動幅小於-3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(TCU, windows = 120) < -0.03"
    
    def rule_216(self):
        # 描述
        self.description = "靜態產能利用率的120天變動幅小於-3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(TCU, windows = 120) < -0.03"

    def rule_217(self):
        # 描述
        self.description = "靜態產能利用率的120天變動幅大於3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(TCU, windows = 120) > 0.03"
    
    def rule_218(self):
        # 描述
        self.description = "動態產能利用率的500天變動幅大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(TCU, windows = 500) > 0.01"
    
    def rule_219(self):
        # 描述
        self.description = "動態產能利用率的500天變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(TCU, windows = 500) < -0.01"

    def rule_220(self):
        # 描述
        self.description = "靜態產能利用率的500天變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(TCU, windows = 500) < -0.01"

    def rule_221(self):
        # 描述
        self.description = "靜態產能利用率的500天變動幅大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(TCU, windows = 500) > 0.01"
    
    def rule_222(self):
        # 描述
        self.description = "動態產能利用率的500天變動幅大於2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(TCU, windows = 500) > 0.02"
    
    def rule_223(self):
        # 描述
        self.description = "動態產能利用率的500天變動幅小於-2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(TCU, windows = 500) < -0.02"
    
    def rule_224(self):
        # 描述
        self.description = "靜態產能利用率的500天變動幅小於-2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(TCU, windows = 500) < -0.02"

    def rule_225(self):
         # 描述
        self.description = "靜態產能利用率的500天變動幅大於2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(TCU, windows = 500) > 0.02"   
    
    def rule_226(self):
        # 描述
        self.description = "動態產能利用率的500天變動幅大於3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(TCU, windows = 500) > 0.03"
    
    def rule_227(self):
        # 描述
        self.description = "動態產能利用率的500天變動幅小於-3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(TCU, windows = 500) < -0.03"

    def rule_228(self):
        # 描述
        self.description = "靜態產能利用率的500天變動幅小於-3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(TCU, windows = 500) < -0.03"

    
    def rule_229(self):
        # 描述
        self.description = "靜態產能利用率的500天變動幅大於3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['TCU']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['TCU']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(TCU, windows = 500) > 0.03"

    def rule_230(self):
        # 描述
        self.description = "動態營建許可的240天變動幅大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PERMIT']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PERMIT']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(PERMIT, windows = 240) > 0.01"
    
    def rule_231(self):
        # 描述
        self.description = "動態營建許可的240天變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PERMIT']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PERMIT']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(PERMIT, windows = 240) < -0.01"

    def rule_232(self):
        # 描述
        self.description = "靜態營建許可的240天變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PERMIT']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PERMIT']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(PERMIT, windows = 240) < -0.01"

    def rule_233(self):
        # 描述
        self.description = "靜態營建許可的240天變動幅大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PERMIT']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PERMIT']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(PERMIT, windows = 240) > 0.01"   

    def rule_234(self):
        # 描述
        self.description = "動態營建許可的240天變動幅大於2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PERMIT']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PERMIT']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(PERMIT, windows = 240) > 0.02"
    
    def rule_235(self):
        # 描述
        self.description = "動態營建許可的240天變動幅小於-2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PERMIT']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PERMIT']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(PERMIT, windows = 240) < -0.02"
    
    def rule_236(self):
        # 描述
        self.description = "靜態營建許可的240天變動幅小於-2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PERMIT']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PERMIT']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(PERMIT, windows = 240) < -0.02"
        
    def rule_237(self):
         # 描述
        self.description = "靜態營建許可的240天變動幅大於2%"

        self.use_data = ['']
        # 資料庫的欄位名稱
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PERMIT']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PERMIT']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(PERMIT, windows = 240) > 0.02"   

    def rule_238(self):
        # 描述
        self.description = "動態營建許可的120天變動幅大於3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PERMIT']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PERMIT']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(PERMIT, windows = 120) > 0.03"
    
    def rule_239(self):
        # 描述
        self.description = "動態營建許可的120天變動幅小於-3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PERMIT']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PERMIT']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(PERMIT, windows = 120) < -0.03"

    def rule_240(self):
        # 描述
        self.description = "靜態營建許可的120天變動幅小於-3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PERMIT']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PERMIT']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(PERMIT, windows = 120) < -0.03"

    def rule_241(self):
        # 描述
        self.description = "靜態營建許可的120天變動幅大於3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PERMIT']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PERMIT']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(PERMIT, windows = 120) > 0.03"
    
    def rule_242(self):
        # 描述
        self.description = "動態營建許可的500天變動幅大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PERMIT']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PERMIT']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(PERMIT, windows = 500) > 0.01"
    
    def rule_243(self):
        # 描述
        self.description = "動態營建許可的500天變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PERMIT']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PERMIT']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(PERMIT, windows = 500) < -0.01"

    def rule_244(self):
        # 描述
        self.description = "靜態營建許可的500天變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PERMIT']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PERMIT']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(PERMIT, windows = 500) < -0.01"


    def rule_245(self):
        # 描述
        self.description = "靜態營建許可的500天變動幅大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PERMIT']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PERMIT']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(PERMIT, windows = 500) > 0.01"

    def rule_246(self):
        # 描述
        self.description = "動態營建許可的500天變動幅大於2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PERMIT']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PERMIT']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(PERMIT, windows = 500) > 0.02"
    
    def rule_247(self):
        # 描述
        self.description = "動態營建許可的500天變動幅小於-2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PERMIT']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PERMIT']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(PERMIT, windows = 500) < -0.02"

    def rule_248(self):
        # 描述
        self.description = "靜態營建許可的500天變動幅小於-2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PERMIT']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PERMIT']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(PERMIT, windows = 500) < -0.02"

    def rule_249(self):
        # 描述
        self.description = "靜態營建許可的500天變動幅大於2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PERMIT']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PERMIT']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(PERMIT, windows = 500) > 0.02"   

    def rule_250(self):
        # 描述
        self.description = "動態營建許可的500天變動幅大於3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PERMIT']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PERMIT']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(PERMIT, windows = 500) > 0.03"
    
    def rule_251(self):
        # 描述
        self.description = "動態營建許可的500天變動幅小於-3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PERMIT']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PERMIT']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(PERMIT, windows = 500) < -0.03"

    def rule_252(self):
        # 描述
        self.description = "靜態營建許可的500天變動幅小於-3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PERMIT']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PERMIT']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(PERMIT, windows = 500) < -0.03"

    def rule_253(self):
        # 描述
        self.description = "靜態營建許可的500天變動幅大於3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PERMIT']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PERMIT']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(PERMIT, windows = 500) > 0.03"

    def rule_254(self):
        # 描述
        self.description = "動態消費者物價指數的240天變動幅大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(CPIAUCSL, windows = 240) > 0.01"
    
    def rule_255(self):
         # 描述
        self.description = "動態消費者物價指數的240天變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(CPIAUCSL, windows = 240) < -0.01"


    def rule_256(self):
        # 描述
        self.description = "靜態消費者物價指數的240天變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(CPIAUCSL, windows = 240) < -0.01"

    def rule_257(self):
        # 描述
        self.description = "靜態消費者物價指數的240天變動幅大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(CPIAUCSL, windows = 240) > 0.01"   
    
    def rule_258(self):
         # 描述
        self.description = "動態消費者物價指數的240天變動幅大於2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(CPIAUCSL, windows = 240) > 0.02"
    
    def rule_259(self):
        # 描述
        self.description = "動態消費者物價指數的240天變動幅小於-2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(CPIAUCSL, windows = 240) < -0.02"

    def rule_260(self):
        # 描述
        self.description = "靜態消費者物價指數的240天變動幅小於-2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(CPIAUCSL, windows = 240) < -0.02"

    def rule_261(self):
        # 描述
        self.description = "靜態消費者物價指數的240天變動幅大於2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(CPIAUCSL, windows = 240) > 0.02"   
    
    def rule_262(self):
         # 描述
        self.description = "動態消費者物價指數的120天變動幅大於3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(CPIAUCSL, windows = 120) > 0.03"
    
    def rule_263(self):
        # 描述
        self.description = "動態消費者物價指數的120天變動幅小於-3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(CPIAUCSL, windows = 120) < -0.03"

    def rule_264(self):
        # 描述
        self.description = "靜態消費者物價指數的120天變動幅小於-3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(CPIAUCSL, windows = 120) < -0.03"

    def rule_265(self):
         # 描述
        self.description = "靜態消費者物價指數的120天變動幅大於3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(CPIAUCSL, windows = 120) > 0.03"

    def rule_266(self):
        # 描述
        self.description = "動態消費者物價指數的500天變動幅大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(CPIAUCSL, windows = 500) > 0.01"
    
    def rule_267(self):
        # 描述
        self.description = "動態消費者物價指數的500天變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(CPIAUCSL, windows = 500) < -0.01"

    def rule_268(self):
        # 描述
        self.description = "靜態消費者物價指數的500天變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(CPIAUCSL, windows = 500) < -0.01"

    def rule_269(self):
         # 描述
        self.description = "靜態消費者物價指數的500天變動幅大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(CPIAUCSL, windows = 500) > 0.01"

    def rule_270(self):
         # 描述
        self.description = "動態消費者物價指數的500天變動幅大於2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(CPIAUCSL, windows = 500) > 0.02"
    
    def rule_271(self):
        # 描述
        self.description = "動態消費者物價指數的500天變動幅小於-2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(CPIAUCSL, windows = 500) < -0.02"
    
    def rule_272(self):
        # 描述
        self.description = "靜態消費者物價指數的500天變動幅小於-2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(CPIAUCSL, windows = 500) < -0.02"

    def rule_273(self):
        # 描述
        self.description = "靜態消費者物價指數的500天變動幅大於2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(CPIAUCSL, windows = 500) > 0.02"   

    def rule_274(self):
         # 描述
        self.description = "動態消費者物價指數的500天變動幅大於3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(CPIAUCSL, windows = 500) > 0.03"
    
    def rule_275(self):
        # 描述
        self.description = "動態消費者物價指數的500天變動幅小於-3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(CPIAUCSL, windows = 500) < -0.03"

    def rule_276(self):
        # 描述
        self.description = "靜態消費者物價指數的500天變動幅小於-3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(CPIAUCSL, windows = 500) < -0.03"

    def rule_277(self):
        # 描述
        self.description = "靜態消費者物價指數的500天變動幅大於3%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(CPIAUCSL, windows = 500) > 0.03"

    def rule_278(self):
        # 描述
        self.description = "動態消費者物價指數的500天變動幅大於4%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(CPIAUCSL, windows = 500) > 0.04"
    
    def rule_279(self):
        # 描述
        self.description = "動態消費者物價指數的500天變動幅小於-4%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(CPIAUCSL, windows = 500) < -0.04"

    def rule_280(self):
        # 描述
        self.description = "靜態消費者物價指數的500天變動幅小於-4%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(CPIAUCSL, windows = 500) < -0.04"

    def rule_281(self):
        # 描述
        self.description = "靜態消費者物價指數的500天變動幅大於4%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(CPIAUCSL, windows = 500) > 0.04"
    
    def rule_282(self):
        # 描述
        self.description = "動態消費者物價指數的500天變動幅大於10%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(CPIAUCSL, windows = 500) > 0.1"

    def rule_283(self):
        # 描述
        self.description = "動態消費者物價指數的500天變動幅小於-10%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(CPIAUCSL, windows = 500) < -0.1"

    def rule_284(self):
        # 描述
        self.description = "靜態消費者物價指數的500天變動幅小於-10%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(CPIAUCSL, windows = 500) < -0.1"

    def rule_285(self):
        # 描述
        self.description = "靜態消費者物價指數的500天變動幅大於10%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(CPIAUCSL, windows = 500) > 0.1"
    
    def rule_286(self):
        # 描述
        self.description = "動態消費者物價指數的500天變動幅大於20%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(CPIAUCSL, windows = 500) > 0.2"
    
    def rule_287(self):
         # 描述
        self.description = "動態消費者物價指數的500天變動幅小於-20%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(CPIAUCSL, windows = 500) < -0.2"



    def rule_288(self):
        # 描述
        self.description = "靜態消費者物價指數的500天變動幅小於-20%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(CPIAUCSL, windows = 500) < -0.2"

    def rule_289(self):
        # 描述
        self.description = "靜態消費者物價指數的500天變動幅大於20%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(CPIAUCSL, windows = 500) > 0.2"

    def rule_290(self):
        # 描述
        self.description = "動態消費者物價指數的500天變動幅大於9%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(CPIAUCSL, windows = 500) > 0.09"
    
    def rule_291(self):
        # 描述
        self.description = "動態消費者物價指數的500天變動幅小於-9%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(CPIAUCSL, windows = 500) < -0.09"

    def rule_292(self):
        # 描述
        self.description = "靜態消費者物價指數的500天變動幅小於-9%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(CPIAUCSL, windows = 500) < -0.09"
    
    def rule_293(self):
        # 描述
        self.description = "靜態消費者物價指數的500天變動幅大於9%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPIAUCSL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPIAUCSL']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(CPIAUCSL, windows = 500) > 0.09"

    def rule_294(self):
        # 描述
        self.description = "動態核心消費者物價指數的240天變動幅大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(CPILFESL, windows = 240) > 0.01"
    
    def rule_295(self):
        # 描述
        self.description = "動態核心消費者物價指數的240天變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(CPILFESL, windows = 240) < -0.01"

    def rule_296(self):
        # 描述
        self.description = "靜態核心消費者物價指數的240天變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(CPILFESL, windows = 240) < -0.01"

    def rule_297(self):
        # 描述
        self.description = "靜態核心消費者物價指數的240天變動幅大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(CPILFESL, windows = 240) > 0.01"   

    def rule_298(self):
        # 描述
        self.description = "動態核心消費者物價指數的240天變動幅大於2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(CPILFESL, windows = 240) > 0.02"
    
    def rule_299(self):
        # 描述
        self.description = "動態核心消費者物價指數的240天變動幅小於-2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(CPILFESL, windows = 240) < -0.02"

    def rule_300(self):
        # 描述
        self.description = "靜態核心消費者物價指數的240天變動幅小於-2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(CPILFESL, windows = 240) < -0.02"

    def rule_301(self):
        # 描述
        self.description = "靜態核心消費者物價指數的240天變動幅大於2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(CPILFESL, windows = 240) > 0.02"   
        
    def rule_302(self):
        # 描述
        self.description = "動態核心消費者物價指數的500天變動幅小於-10%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(CPILFESL, windows = 500) < -0.1"

    def rule_303(self):
        # 描述
        self.description = "動態核心消費者物價指數的500天變動幅大於10%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(CPILFESL, windows = 500) > 0.1"

    def rule_304(self):
        # 描述
        self.description = "靜態核心消費者物價指數的500天變動幅小於-10%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(CPILFESL, windows = 500) < -0.1"

    def rule_305(self):
         # 描述
        self.description = "靜態核心消費者物價指數的500天變動幅大於10%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(CPILFESL, windows = 500) > 0.1"

    def rule_306(self):
        # 描述
        self.description = "動態核心消費者物價指數的500天變動幅大於20%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(CPILFESL, windows = 500) > 0.2"
        
    def rule_307(self):
        # 描述
        self.description = "動態核心消費者物價指數的500天變動幅小於-20%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(CPILFESL, windows = 500) < -0.2"

    def rule_308(self):
        # 描述
        self.description = "靜態核心消費者物價指數的500天變動幅小於-20%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(CPILFESL, windows = 500) < -0.2"

    def rule_309(self):
        # 描述
        self.description = "靜態核心消費者物價指數的500天變動幅大於20%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(CPILFESL, windows = 500) > 0.2"

    def rule_310(self):
        # 描述
        self.description = "動態核心消費者物價指數的500天變動幅大於9%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(CPILFESL, windows = 500) > 0.09"
    
    def rule_311(self):
        # 描述
        self.description = "動態核心消費者物價指數的500天變動幅小於-9%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(CPILFESL, windows = 500) < -0.09"

    def rule_312(self):
        # 描述
        self.description = "靜態核心消費者物價指數的500天變動幅小於-9%"

        # 資料庫的欄位名稱  
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(CPILFESL, windows = 500) < -0.09"

    def rule_313(self):
        # 描述
        self.description = "靜態核心消費者物價指數的500天變動幅大於9%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(CPILFESL, windows = 500) > 0.09"
    
    def rule_314(self):
        # 描述
        self.description = "動態核心消費者物價指數的500天變動幅大於8%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(CPILFESL, windows = 500) > 0.08"

    def rule_315(self):
        # 描述
        self.description = "動態核心消費者物價指數的500天變動幅小於-8%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(CPILFESL, windows = 500) < -0.08"

    def rule_316(self):
        # 描述
        self.description = "靜態核心消費者物價指數的500天變動幅小於-8%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(CPILFESL, windows = 500) < -0.08"
    
    def rule_317(self):
        # 描述
        self.description = "靜態核心消費者物價指數的500天變動幅大於8%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(CPILFESL, windows = 500) > 0.08"

    def rule_318(self):
        # 描述
        self.description = "動態核心消費者物價指數的500天變動幅大於7%"

         # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(CPILFESL, windows = 500) > 0.07"
    
    def rule_319(self):
        # 描述
        self.description = "動核心消費者物價指數的500天變動幅小於-7%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(CPILFESL, windows = 500) < -0.07"
    
    def rule_320(self):
        # 描述
        self.description = "靜態核心消費者物價指數的500天變動幅小於-7%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(CPILFESL, windows = 500) < -0.07"
    
    def rule_321(self):
        # 描述
        self.description = "靜態核心消費者物價指數的500天變動幅大於7%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['CPILFESL']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['CPILFESL']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(CPILFESL, windows = 500) > 0.07"

    def rule_322(self):
        # 描述
        self.description = "動態非農就業指數的240天變動幅大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(PAYEMS, windows = 240) > 0.01"

    def rule_323(self):
        # 描述
        self.description = "動態非農就業指數的240天變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(PAYEMS, windows = 240) < -0.01"
    
    def rule_324(self):
        # 描述
        self.description = "靜態非農就業指數的240天變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(PAYEMS, windows = 240) < -0.01"

    def rule_325(self):
        # 描述
        self.description = "靜態非農就業指數的240天變動幅大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(PAYEMS, windows = 240) > 0.01"   

    def rule_326(self):
        # 描述
        self.description = "動態非農就業指數的240天變動幅大於2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(PAYEMS, windows = 240) > 0.02"
        
    def rule_327(self):
        # 描述
        self.description = "動態非農就業指數的240天變動幅小於-2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(PAYEMS, windows = 240) < -0.02"

    def rule_328(self):
        # 描述
        self.description = "靜態非農就業指數的240天變動幅小於-2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(PAYEMS, windows = 240) < -0.02"

    def rule_329(self):
        # 描述
        self.description = "靜態非農就業指數的240天變動幅大於2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(PAYEMS, windows = 240) > 0.02"   

    def rule_330(self):
        # 描述
        self.description = "動態非農就業指數的500天變動幅小於-10%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(PAYEMS, windows = 500) < -0.1"


    def rule_331(self):
        # 描述
        self.description = "動態非農就業指數的500天變動幅大於10%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(PAYEMS, windows = 500) > 0.1"
    
    def rule_332(self):
        # 描述
        self.description = "靜態非農就業指數的500天變動幅小於-10%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(PAYEMS, windows = 500) < -0.1"

    def rule_333(self):
        # 描述
        self.description = "靜態非農就業指數的500天變動幅大於10%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(PAYEMS, windows = 500) > 0.1"
    
    def rule_334(self):
        # 描述
        self.description = "動態非農就業指數的120天變動幅大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(PAYEMS, windows = 120) > 0.01"

    def rule_335(self):
        # 描述
        self.description = "動態非農就業指數比120天前變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(PAYEMS, windows = 120) < -0.01"

    def rule_336(self):
        # 描述
        self.description = "靜態非農就業指數的120天變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(PAYEMS, windows = 120) < -0.01"

    def rule_337(self):
        # 描述
        self.description = "靜態非農就業指數的120天變動幅大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(PAYEMS, windows = 120) > 0.01"   

    def rule_338(self):
         # 描述
        self.description = "動態非農就業指數比120天前變動幅大於2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(PAYEMS, windows = 120) > 0.02"
    
    def rule_339(self):
        # 描述
        self.description = "動態非農就業指數比120天前變動幅小於-2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(PAYEMS, windows = 120) < -0.02"
    
    def rule_340(self):
        # 描述
        self.description = "靜態非農就業指數的120天變動幅小於-2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(PAYEMS, windows = 120) < -0.02"
    
    def rule_341(self):
        # 描述
        self.description = "靜態非農就業指數的120天變動幅大於2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PAYEMS']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PAYEMS']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(PAYEMS, windows = 120) > 0.02"   
    
    def rule_342(self):
        # 描述
        self.description = "動態生產者物價指數比120天前變動幅大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PPIACO']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PPIACO']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(PPIACO, windows = 120) > 0.01"
    
    def rule_343(self):
        # 描述
        self.description = "動態生產者物價指數比120天前變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PPIACO']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PPIACO']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(PPIACO, windows = 120) < -0.01"
    
    def rule_344(self):
        # 描述
        self.description = "靜態生產者物價指數的120天變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PPIACO']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PPIACO']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(PPIACO, windows = 120) < -0.01"

    def rule_345(self):
        # 描述
        self.description = "靜態生產者物價指數的120天變動幅大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PPIACO']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PPIACO']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(PPIACO, windows = 120) > 0.01"   

    def rule_346(self):
        # 描述
        self.description = "動態生產者物價指數比120天前變動幅大於2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PPIACO']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PPIACO']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(PPIACO, windows = 120) > 0.02"
    
    def rule_347(self):
        # 描述
        self.description = "動態生產者物價指數比120天前變動幅小於-2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PPIACO']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PPIACO']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(PPIACO, windows = 120) < -0.02"
        
    def rule_348(self):
        # 描述
        self.description = "靜態生產者物價指數的120天變動幅小於-2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PPIACO']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PPIACO']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(PPIACO, windows = 120) < -0.02"

    def rule_349(self):
        # 描述
        self.description = "靜態生產者物價指數的120天變動幅大於2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PPIACO']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PPIACO']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(PPIACO, windows = 120) > 0.02"   

    def rule_350(self):
        # 描述
        self.description = "動態生產者物價指數比240天前變動幅大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PPIACO']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PPIACO']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(PPIACO, windows = 240) > 0.01"
    
    def rule_351(self):
        # 描述
        self.description = "動態生產者物價指數比240天前變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PPIACO']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PPIACO']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(PPIACO, windows = 240) < -0.01"

    def rule_352(self):
        # 描述
        self.description = "靜態生產者物價指數的240天變動幅小於-1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PPIACO']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PPIACO']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(PPIACO, windows = 240) < -0.01"

    def rule_353(self):
        # 描述
        self.description = "靜態生產者物價指數的240天變動幅大於1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PPIACO']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PPIACO']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(PPIACO, windows = 240) > 0.01"   
    
    def rule_354(self):
         # 描述
        self.description = "動態生產者物價指數比240天前變動幅大於2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PPIACO']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PPIACO']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(PPIACO, windows = 240) > 0.02"
        
    def rule_355(self):
        # 描述
        self.description = "動態生產者物價指數比240天前變動幅小於-2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PPIACO']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PPIACO']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(PPIACO, windows = 240) < -0.02"

    def rule_356(self):
        # 描述
        self.description = "靜態生產者物價指數的240天變動幅小於-2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PPIACO']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PPIACO']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(PPIACO, windows = 240) < -0.02"
    
    def rule_357(self):
        # 描述
        self.description = "靜態生產者物價指數的240天變動幅大於2%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PPIACO']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PPIACO']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(PPIACO, windows = 240) > 0.02"   
    
    def rule_358(self):
        # 描述
        self.description = "動態生產者物價指數比500天前變動幅小於-10%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PPIACO']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PPIACO']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(PPIACO, windows = 500) < -0.1"
    
    def rule_359(self):
        # 描述
        self.description = "動態生產者物價指數比500天前變動幅大於10%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PPIACO']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PPIACO']

        # 處理變數
        self.process_variable = "percent_change_track_adjusted_values_change(PPIACO, windows = 500) > 0.1"

    def rule_360(self):
        # 描述
        self.description = "靜態生產者物價指數的500天變動幅小於-10%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PPIACO']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PPIACO']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(PPIACO, windows = 500) < -0.1"

    def rule_361(self):
        # 描述
        self.description = "靜態生產者物價指數的500天變動幅大於-10%"

        # 資料庫的欄位名稱
        self.use_data = ['']
    
        # measure檔案名稱
        self.cross_section_data_file_name = ['PPIACO']
    
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['PPIACO']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(PPIACO, windows = 500) > 0.1"