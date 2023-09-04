liste = []
for i in range(5):
    code = input("")
    if "FBI" in code:
        liste.append(i+1)
    liste = sorted(liste) 
if liste:
    for i in range(len(liste)):
        print(liste[i], end=" ")
else:
    print("HE GOT AWAY!")