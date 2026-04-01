scores = [250, 480, 310, 95, 720, 60, 487,165]
def afficher_scores(liste):
    print("Scores :", liste)

afficher_scores(scores)


def afficher_top3(liste): 
    scores_tries = sorted(liste, reverse=True) 
    top_3 = scores_tries[:3] 
    print(f"Top 3 scores :", top_3)

afficher_top3(scores)


def afficher_niveau(liste):
    for i in liste :
        if i >= 700:
         print(f"{i} = expert")
        elif i >= 400:
         print(f"{i} = avancé")
        elif i < 400:
         print(f"{i} = débutant")

afficher_niveau(scores)












