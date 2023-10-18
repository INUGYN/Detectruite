@echo off
:Start
rem Vérification de l'installation de Python avec Chocolatey

rem Vérifier si Chocolatey est installé
choco --version
if %errorlevel% neq 0 (
    echo Chocolatey n'est pas installé. Installation de Chocolatey...
    @powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"
    if %errorlevel% neq 0 (
        echo L'installation de Chocolatey a échoué. Veuillez installer Chocolatey manuellement et réessayez.
        goto :Start
    )
    echo Chocolatey a été installé avec succès.
    goto :Start
) else (
    echo Chocolatey est déjà installé.
    goto :2
)
:2
rem Vérifier si Python est installé
python --version
if %errorlevel% neq 0 (
    echo Python n'est pas installé. Installation de Python...
    choco install python311 -y
    if %errorlevel% neq 0 (
        echo L'installation de Python a échoué. Veuillez installer Python manuellement et réessayez.
        goto :Start
    ) else (
        echo Python a été installé avec succès.
        goto :Start
    )
) else (
    echo Python est déjà installé.
    goto :3
)
:3
cd..
pip install --upgrade --pre --extra-index-url https://marcelotduarte.github.io/packages/ cx_Freeze
pip install pyshortcuts
pip install opencv-python
pip install numpy
pip install pandas
pip install pillow
pip install matplotlib
pip install plyer
pip install pyWebBrowser
pip install winsound


set "repertoire=%~dp0"

pushd "%repertoire%/code detecte/dependance"

python -m pip install requests

popd

pushd "%repertoire%"

python setup.py build

pushd "%repertoire%/code detecte/dependance"

python message.py

popd

exit