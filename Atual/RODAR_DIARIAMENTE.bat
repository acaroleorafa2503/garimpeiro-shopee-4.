@echo off
cd /d %~dp0
call .venv\Scripts\activate
python run_daily.py
python generate_report.py
