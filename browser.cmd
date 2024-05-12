@echo off
set "checkfile=__init__.py"
set "lib1=PyQt5"
set "lib2=configparser"

if exist %checkfile% (
    REM EXISTS
    goto step2
) else (
    REM NOT EXISTS
    echo Cannot find REQUIRED files to run BrowserPy.
    echo Make a fresh reinstall of BrowserPy and try again.
    echo Press any key to exit
    pause >nul
    exit /b
)

:step2
python --version > nul 2>&1
if %errorlevel% equ 0 (
    REM PYTHON INSTALLED
    goto step3
) else (
    REM PYTHON NOT INSTALLED
    echo Python not installed.
    echo Install python and come back later.
    echo Press any key to exit.
    pause >nul
    exit /b
)

:step3
cls
pip show %lib1% > nul 2>&1
if %errorlevel% equ 0 (
    REM LIB1 INSTALLED
    goto step4
) else (
    REM LIB1 NOT INSTALLED
    echo Required library not installed.
    echo Installing library %lib1%...
    pip install %lib1%
    if %errorlevel% equ 0 (
        REM INSTALLED LIB WITH SUCCESS
        echo Library installation exit with code 0
        echo Do you want to retry the verification now?
        goto step4
    ) else (
        REM INSTALLED LIB WITH ERRORS
        echo Library installation exit with code 1
        echo Library not installed. Installation with errors.
        echo Press any key to exit.
        pause >nul
        exit /b
    )
)

:step4
cls
pip show %lib1% > nul 2>&1
if %errorlevel% equ 0 (
    REM LIB2 INSTALLED
    goto run
) else (
    REM LIB2 NOT INSTALLED
    echo Required library not installed.
    echo Installing library %lib2%...
    pip install %lib2%
    if %errorlevel% equ 0 (
        REM INSTALLED LIB WITH SUCCESS
        echo Library installation exit with code 0
        echo Do you want to retry the verification now?
        goto step4
    ) else (
        REM INSTALLED LIB WITH ERRORS
        echo Library installation exit with code 1
        echo Library not installed. Installation with errors.
        echo Press any key to exit.
        pause >nul
        exit /b
    )
)

:run
cls
python %cd%/browser.py
echo.
echo App closed.
echo Press any key to exit.
pause >nul
exit /b
