@echo off
REM Lanzador de la app PokeAPI (Windows).
REM Crea el entorno virtual la primera vez, instala dependencias y muestra un menu.

setlocal enabledelayedexpansion
cd /d "%~dp0"

if not exist venv (
    echo Creando entorno virtual...
    python -m venv venv
    if errorlevel 1 (
        echo No se pudo crear el entorno virtual. Verifica que Python este instalado.
        pause
        exit /b 1
    )
)

call venv\Scripts\activate.bat

python -c "import requests" >nul 2>&1
if errorlevel 1 (
    echo Instalando dependencias...
    pip install -r requirements.txt
)

if not exist .env (
    copy .env.example .env >nul
)

:menu
cls
echo ============================================
echo   Consultas a la PokeAPI - Laboratorio 3
echo ============================================
echo.
echo   1. Consultar uno o varios Pokemon
echo   2. Ver Pokemon guardados
echo   3. Correr las pruebas (pytest)
echo   4. Salir
echo.
set /p opcion="Elige una opcion (1-4): "

if "%opcion%"=="1" goto consultar
if "%opcion%"=="2" goto listar
if "%opcion%"=="3" goto pruebas
if "%opcion%"=="4" goto fin
goto menu

:consultar
echo.
set /p nombres="Escribe uno o varios nombres separados por espacio: "
python -m src.main %nombres%
echo.
pause
goto menu

:listar
echo.
python -m src.main --listar
echo.
pause
goto menu

:pruebas
echo.
pip install -r requirements-dev.txt >nul
python -m pytest
echo.
pause
goto menu

:fin
endlocal
exit /b 0
