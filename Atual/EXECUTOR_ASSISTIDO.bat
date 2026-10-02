@echo off
cd /d %~dp0
call .venv\Scripts\activate
python orchestrator.py
python executor_assistido.py
start "" http://localhost:8501
streamlit run app.py
pause
