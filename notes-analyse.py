listes_notes=[6,18,13]
listes_notes.sort()
def compter_reussites(listes):
      compter=0
      for i in listes:
            if i>=10:
                  compter+=1
      return compter  
print(compter_reussites(listes_notes))
def afficher_mention(moyenne):
      for i in moyenne:
            if i>=16:
                  print(f"pour la note {i} la mention est très bien")
            elif i>=14:
                  print(f"pour la note {i} la mention est bien") 
            elif i>=12:
                  print(f"pour la note {i} la mention est assez bien")
            elif i>=10:
                  print(f"pour la note {i} la mention est passable")
            else:
                  print(f"pour la note {i} la mention est insuffisant")
                  



