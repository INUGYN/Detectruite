import os
import shutil
import pyshortcuts
from pathlib import Path
from pyshortcuts import make_shortcut
from cx_Freeze import setup, Executable

repertoire = os.path.dirname(os.path.abspath(__file__))
repertoire = os.path.normpath(repertoire)
repertoire_files = f"{repertoire}/code detecte"

# Chemin vers le dossier de destination dans C:/Program Files
program = os.path.join("C:/Program Files")
code = os.path.join(program, "Détectruite")
code_destination = os.path.join(program, "Détectruite/code detecte")

# Supprimer le répertoire de destination s'il existe déjà
if os.path.exists(code):
    shutil.rmtree(code)
        

# Créez le répertoire de destination s'il n'existe pas déjà
os.makedirs(code, exist_ok=True)

# Copiez le répertoire avec son contenu
shutil.copytree(repertoire_files, code_destination)

build = os.path.join(program, "Détectruite/build")
os.makedirs(build, exist_ok=True)

# Chemin vers le script Python
script = f"{program}/Détectruite/code detecte/Détectruite.py"

icon = f"{program}/Détectruite/code detecte/image/truite.ico"

# Configuration de l'exécutable
exe = Executable(
    script=script,
    base="Win32GUI",
    icon=icon,
)

# Options de configuration supplémentaires
options = {
    "build_exe": {
        "packages": [],  # Liste des packages supplémentaires à inclure
        "excludes": [],  # Liste des modules à exclure
        "include_files": [],  # Liste des fichiers supplémentaires à inclure
        "build_exe": build  # Crée le fichier exécutable dans le dossier "C:/Program Files/detectruite"
    }
}

# Création de l'installation
setup(
    name="Détectruite",
    executables=[exe],
    options=options,
)

# Chemin vers le fichier exécutable
executable_path = f"{build}/Détectruite.exe"



# Nom du raccourci
shortcut_name = "Détectruite"

# Emplacement où vous souhaitez sauvegarder le raccourci (par exemple, le bureau)
shortcut_location = Path.home() / "Desktop"

try:
    racourcis = Path.home() / "Desktop/Détectruite.lnk"
    os.remove(racourcis)
except:
    pass
make_shortcut(executable_path, name='Détectruite', icon=icon, executable=executable_path)