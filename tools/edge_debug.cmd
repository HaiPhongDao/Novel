@echo off
rem Bấm đúp để mở Edge cho aistudio_run.py; "edge_debug.cmd -Login" để đăng nhập lần đầu.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0edge_debug.ps1" %*
