@echo off
setlocal ENABLEEXTENSIONS ENABLEDELAYEDEXPANSION

REM Kodowanie konsoli na UTF-8 (dla polskich znakow)
chcp 65001 >nul

REM Przejdz do folderu z tym plikiem
cd /d "%~dp0"

REM Sprawdz dostepnosc Pythona (python lub py)
set "PYEXE="
where python >nul 2>nul && set "PYEXE=python"
if not defined PYEXE (
  where py >nul 2>nul && set "PYEXE=py"
)
if not defined PYEXE (
  echo [BLAD] Nie znaleziono Pythona w PATH.
  echo Zainstaluj Python 3.10+: https://www.python.org/downloads/
  pause
  goto :eof
)

REM Instalacja zaleznosci
"%PYEXE%" -m pip install --upgrade pip
if exist requirements.txt (
  echo [INFO] Instalacja zaleznosci z requirements.txt ...
  "%PYEXE%" -m pip install -r requirements.txt
  if errorlevel 1 (
    echo [BLAD] Instalacja zaleznosci nie powiodla sie.
    pause
    goto :eof
  )
) else (
  echo [UWAGA] Nie znaleziono pliku requirements.txt. Pomijam instalacje.
)

REM Uruchom program
if exist src\main.py (
  echo [INFO] Uruchamiam program ...
  "%PYEXE%" src\main.py
) else (
  echo [BLAD] Nie znaleziono pliku src\main.py
)

REM Zatrzymaj okno, aby pokazac wynik
pause

endlocal
