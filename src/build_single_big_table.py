import analysis as analysis
from pathlib import Path

obj_analysis = analysis.RunEvaluate()
obj_analysis.main_for_single_rule() # 單一rule 
obj_analysis.build_combine_table(only_sigle_rule=True)
