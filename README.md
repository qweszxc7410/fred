```mermaid
graph TB
  %% 階段一
  A1[階段一：取得 FRED API 並寫入 .env]
  A2[執行 get_data.py 抓資料]
  A3[執行 measure_build.py 建立 measure.pt]
  A4[執行 rule_build.py 建立 rule.pt]
  A5[執行 build_single_big_table.py 分析輸出 csv]
  A6[執行 combine_rule_username.py 產生隨機組合]
  A7[執行 plot.py 繪製圖表]

  A1 --> A2 --> A3 --> A4 --> A5 --> A6 --> A7

  %% 階段二
  B1[階段二：修改 rule_library_username.py 檔名]
  B2[新增規則（參考範例）]

  A7 --> B1 --> B2
