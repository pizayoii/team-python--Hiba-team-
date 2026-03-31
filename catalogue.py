from pathlib import Path

# Définir le chemin du fichier
file_path = r'c:\Users\rakhi\OneDrive\Bureau\cours_git\tp-git-groupe\team-python--Hiba-team-\catalogue.txt'

# 1. Lire et afficher le catalogue
films = []
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        next(f)  # Ignorer le commentaire
        next(f)  # Ignorer l'en-tête
        for line in f:
            line = line.strip()
            if line:  # Ignorer lignes vides
                parts = line.split(';')
                if len(parts) == 4:
                    films.append({'titre': parts[0], 'annee': parts[1], 'real': parts[2], 'note': float(parts[3])})
except FileNotFoundError:
    print("Erreur : fichier non trouvé")
    exit()
    
