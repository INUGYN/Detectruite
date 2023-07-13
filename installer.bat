@echo off

set "repertoire=%~dp0"

cd %repertoire%/code detecte/dependance

python -m pip install requests

pip install -r requirements.txt

cd ..
cd ..

python setup.py build

cd %repertoire%/code detecte/dependance

python message.py

exit
