@echo off
cd /d %~dp0
call .venv\Scripts\activate
python import_performance.py
python import_inventory.py
python run_daily.py
python portfolio.py
python cash_inventory.py
python growth_planner.py
pause
