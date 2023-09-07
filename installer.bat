@echo off

set "repertoire=%~dp0"

pushd "%repertoire%/code detecte/dependance"

python -m pip install requests

pip install pyshortcuts

pip install -r requirements.txt

popd

pushd "%repertoire%"

python setup.py build

pushd "%repertoire%/code detecte/dependance"

python message.py

popd

exit
