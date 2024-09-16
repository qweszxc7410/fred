

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
        self.description = "靜態美國GDP原始數字比250天前看到的減少"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['GDPC1']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['GDPC1']

        # 處理變數
        self.process_variable = "diff_record_daily_value_change(GDPC1,windows = 250) <  0 "
    
    def rule_2(self):
        # 描述
        self.description = "靜態美國GDP原始數字比250天前看到的增加"

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
        self.description = "動態美國GDP原始數字比250天前看到的減少"

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
        self.description = "動態美國GDP原始數字比250天前看到的增加"

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
        self.description = "動態美國GDP原始數字比250天前減少1%"

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
        self.description = "靜態美國GDP原始數字比250天前增加1%"

        # 資料庫的欄位名稱
        self.use_data = ['']
        
        # measure檔案名稱
        self.cross_section_data_file_name = ['GDPC1']
        
        # measure檔案名稱對應的變數名稱
        self.cross_section_data = ['GDPC1']

        # 處理變數
        self.process_variable = "percent_change_record_daily_value_change(GDPC1,windows = 250) > 0.01 "