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
   
            if i>=16:
                  return " la mention est très bien"
            elif i>=14:
                  return "la mention est bien"
            elif i>=12:
                  return "la mention est assez bien"
            elif i>=10:
                  return " la mention est passable"
            else:
                  return " la mention est insuffisant"

moyen=0.0                  
for i in listes_notes:
      moyen=moyen+i/len(listes_notes)

print(afficher_mention(moyen))

