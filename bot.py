import os

def create_file():
    # Demander à l'utilisateur le nom du fichier et l'extension
    filename = input("Entrez le nom du fichier (sans extension) : ")
    extension = input("Entrez l'extension du fichier (ex: txt, md, py, etc.) : ")

    # Construire le chemin complet du fichier
    file_path = f"{filename}.{extension}"

    try:
        # Créer le fichier dans le dossier où se trouve le script
        with open(file_path, 'w') as file:
            file.write("")  # Écrire un contenu vide dans le fichier
        print(f"Le fichier {file_path} a été créé avec succès.")
    except Exception as e:
        print(f"Une erreur est survenue lors de la création du fichier : {e}")

# Lancer la fonction
create_file()
