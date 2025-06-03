#!/bin/bash

# 設定根目錄
SRC_DIR="./src"

# 步驟 2: 從 FRED 抓資料
echo "📥 [2/6] 執行 get_data.py 抓取 FRED 資料..."
python "$SRC_DIR/get_data.py"

# 步驟 3: 建立 measure.pt
echo "📊 [3/6] 執行 measure_build.py 建立 measure.pt..."
python "$SRC_DIR/measure_build.py"

# 步驟 4: 建立 rule.pt
echo "📏 [4/6] 執行 rule_build.py 建立 rule.pt..."
python "$SRC_DIR/rule_build.py"

# 步驟 5: 產出 single_table_long.csv / short.csv
echo "📈 [5/6] 執行 build_single_big_table.py 分析結果..."
python "$SRC_DIR/build_single_big_table.py"

# 步驟 6: 產出隨機組合的 combine_rule
echo "🔀 [6/6] 執行 combine_rule_username.py 產生隨機組合..."
python "$SRC_DIR/combine_rule_username.py"

# 步驟 7: 繪圖
echo "🖼️ [完成] 執行 plot.py 繪製圖表..."
python "$SRC_DIR/plot.py"

echo "✅ 所有流程已完成！"

