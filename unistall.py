import os
import shutil

def unistall():
    folder_path = os.path.dirname(os.path.abspath(__file__))
    print(f"Suppression du dossier : {folder_path}")
    shutil.rmtree(folder_path, ignore_errors=True)

if __name__ == "__main__":
    unistall()
