import csv

with open ("depenses.csv", "r", encoding="utf-8") as fichier :
    lecteur = csv.DictReader(fichier)
    total_depense = []
    depense_alimentation = []
    depense_loisirs = []
    depense_transport = []
    for ligne in lecteur :
        print (f"{ligne ['date']} | {ligne['categorie']} | {ligne ['description']} | {ligne ['montant']}")
        total_depense.append(float(ligne["montant"]))
        if ligne["categorie"] == "Alimentation" :
            depense_alimentation.append(float(ligne["montant"]))
        elif ligne["categorie"] == "Loisirs" :
            depense_loisirs.append(float(ligne["montant"]))
        elif ligne["categorie"] == "Transport" :
            depense_transport.append(float(ligne["montant"]))
max_depense = max(total_depense)
min_depense = min(total_depense)




print("")
print (f"La somme de toutes les dépenses est égal à : {sum(total_depense)}")
print (f"La somme des dépenses dans l'alimentation est égal à : {sum(depense_alimentation)}.")
print (f"La somme des dépenses dans les loisirs est égal à : {sum(depense_loisirs)}.")
print(f"La somme des dépenses dans le transport est égal à : {sum(depense_transport)}.")
print ("")
print ("")
print (f"La plus grande dépenses est de : {max_depense}.")
print (f"La plus petite dépenses est de : {min_depense}.")
