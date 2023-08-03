def tourner(chaine , tab) :
    nombre = 0
    for letter in chaine :
        nombre += tab.index(letter)

    for i in range(len(chaine)) :
        j = (tab.index(chaine[i])+nombre) % 26
        chaine[i] = tab[j]

    return chaine

def fusion(chaine1 , chaine2, tab) :
    for i in range(len(chaine1)) :
        j = (tab.index(chaine2[i]) + tab.index(chaine1[i])) % 26
        chaine1[i] = tab[j]

    return chaine1

tableau_majuscules = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
s = input()

tete = list(s[:len(s)//2])
queu = list(s[len(s)//2:])

tete = tourner(tete , tableau_majuscules)
queu = tourner(queu , tableau_majuscules)

tete = fusion(tete , queu , tableau_majuscules)

print(''.join(tete))