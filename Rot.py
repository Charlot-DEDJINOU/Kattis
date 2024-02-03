alphabet_majuscules = [chr(65 + i) for i in range(26)]
alphabet_majuscules.append("_")
alphabet_majuscules.append(".")

def ROT(message, cle) :
    shiffer = ""
    for letter in message :
        shiffer += alphabet_majuscules[(alphabet_majuscules.index(letter) + cle) % 28]
    
    return shiffer


message = input()
rotate = int(input())
print(ROT(message, rotate))