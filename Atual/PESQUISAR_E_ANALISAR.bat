@echo off
cd /d %~dp0
call .venv\Scripts\activate
set /p BRAVE_SEARCH_API_KEY=Digite sua chave Brave Search API:
python run_public_research.py
python run_daily.py
python generate_report.py
pause
