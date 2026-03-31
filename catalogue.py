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
    
# 2. Afficher chaque film
print("=== Catalogue complet ===")
for film in films:
    print(f"{film['titre']} ({film['annee']}) - Realisateur : {film['real']} - Note : {int(film['note'])}/10")   
    
# 3. Films avec note >= 9
print("\n=== Films avec note >= 9 ===")
films_notes = [f for f in films if f['note'] >= 9]
if films_notes:
    for film in films_notes:
        print(f"{film['titre']} ({film['annee']}) - Realisateur : {film['real']} - Note : {int(film['note'])}/10")
else:
    print("Aucun film avec note >= 9") 
    
# 4. Moyenne des notes
if films:
    moyenne = sum(film['note'] for film in films) / len(films)
    print(f"\nNote moyenne : {moyenne:.2f}/10")    
