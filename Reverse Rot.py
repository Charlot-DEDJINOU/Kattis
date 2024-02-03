alphabet_majuscules = [chr(65 + i) for i in range(26)]
alphabet_majuscules.append("_")
alphabet_majuscules.append(".")

def ROT(message, cle) :
    shiffer = ""
    for letter in message :
        shiffer += alphabet_majuscules[(alphabet_majuscules.index(letter) + cle) % len(alphabet_majuscules)]
    
    return shiffer


while True :
    s = input()
    if s == "0" :
        break
    
    s = s.split()
    rotate = int(s[0])
    message = "".join([s[1][x] for x in range(len(s[1]) - 1 , -1 ,-1)])

    print(ROT(message, rotate))

