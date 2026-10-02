@echo off
cd /d %~dp0
call .venv\Scripts\activate
python import_performance.py
python -c "from learning import calibrate_weights; print(calibrate_weights(False))"
pause
