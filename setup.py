import os
import pyshortcuts
from pyshortcuts import make_shortcut
from cx_Freeze import setup, Executable
from pathlib import Path

repertoire = os.path.dirname(os.path.abspath(__file__))
repertoire = os.path.normpath(repertoire)

# Chemin vers le dossier de destination dans C:/Program Files
program = os.path.join("C:/Program Files/Détectruite")

# Chemin vers le script Python
script = f"{repertoire}/code detecte/Détectruite.py"

icon = f"{repertoire}/code detecte/image/truite.ico"

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
        "build_exe": program  # Crée le fichier exécutable dans le dossier "C:/Program Files/detectruite"
    }
}

# Création de l'installation
setup(
    name="Détectruite",
    executables=[exe],
    options=options,
)

# Chemin vers le fichier exécutable
executable_path = f"{program}\\Détectruite.exe"

# Nom du raccourci
shortcut_name = "Détectruite"

# Emplacement où vous souhaitez sauvegarder le raccourci (par exemple, le bureau)
shortcut_location = Path.home() / "Desktop"

make_shortcut(executable_path, name='Détectruite', icon=icon, executable=executable_path)
