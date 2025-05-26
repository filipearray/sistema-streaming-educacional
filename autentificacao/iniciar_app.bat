@echo off
cd /d %~dp0
start "" "dist\main.exe"
timeout /t 2 >nul
start http://127.0.0.1:5000/register
