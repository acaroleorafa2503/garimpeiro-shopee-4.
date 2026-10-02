
@echo off
cd /d %~dp0
if not exist .venv (
  py -m venv .venv
)
call .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python seed.py
python scheduler.py
start "" http://localhost:8501
streamlit run app.py
pause
