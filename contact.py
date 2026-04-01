
contacts = []
with open("contacts.txt", "r") as f:
    for ligne in f:
        nom, email, tel = ligne.strip().split("|")
        contacts.append([nom, email, tel])
        print(nom, "→", email, "/", tel)
rech = input("\n saisir un nom : ")
trouve = False
for c in contacts:
    if rech.lower() in c[0].lower():
        print("Trouvé :", c[0], c[1], c[2])
        trouve = True
if not trouve:
    print("Contact introuvable")
nom = input("\nNom : ")
email = input("Email : ")
tel = input("Tel : ")
contacts.append([nom, email, tel])
with open("contacts.txt", "w") as f:
    for c in contacts:
        f.write(c[0] + "|" + c[1] + "|" + c[2] + "\n")
print("Total :", len(contacts))