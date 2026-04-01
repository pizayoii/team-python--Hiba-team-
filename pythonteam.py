import csv 
with open("team.csv", "r", encoding="utf-8") as fichier: 
    lecteur = csv.DictReader(fichier) 
    for ligne in lecteur: 
        print(f"equipe: {ligne['equipe']}, victoires: {ligne['victoires']} , nuls: {ligne['nuls']} , defaites: {ligne['defaites']}") 
tampon=[]
with open("team.csv", "r", newline="", encoding="utf-8") as fichier:
    team_write=csv.reader(fichier)
    for i, line in enumerate(team_write):
        if i==0:
            line.append("points")
            tampon.append(line)
           # tampon.append("points")  
            continue
        #print(f"this is {tampon[0]}")
        equipe,victoires,nuls,defaites,points=line[0],line[1],line[2],line[3],[]
        points.append(int(victoires)*3 +int(nuls))
        tampon.append([equipe,victoires,nuls,defaites,points])  

with open("new_team.csv", "w", newline="", encoding="utf-8") as fichier:
    csv_writer=csv.writer(fichier)
    csv_writer.writerows(tampon)        


