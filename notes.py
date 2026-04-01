notes = [12, 8, 15, 9, 17]
notes.extend([7, 14, 11])

def afficher_notes(liste):
    print("Notes :", liste)
afficher_notes(notes)
def calculer_moyenne(liste):
    return round(sum(liste) / len(liste), 1)

print("Moyenne :", calculer_moyenne(notes))