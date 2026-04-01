scores = [250, 480, 310, 95, 720, 150, 888, 430]
def afficher_scores(liste):
    print("Scores :", liste)

afficher_scores(scores)



def calculer_total(liste) :
    somme = sum(liste)
    print (f"La somme est égal à :", somme)
    return somme
print(calculer_total(scores))



def calculer_moyenne(liste) :
    moyenne =  sum(liste) / len(liste)
    print (f"La moyenne est égal à : ", round(moyenne, 2))
    return moyenne
print (calculer_moyenne(scores))