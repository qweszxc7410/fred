@echo on
chcp 65001 
call C:\ProgramData\Anaconda3\Scripts\activate.bat  C:\Users\chube\.conda\envs\EconomicAnalysis
cd /d D:\EconomicAnalysis
python daily_run.py
timeout /t 10800 /nobreak