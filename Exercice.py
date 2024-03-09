def cesar() :
    alphabet_majuscules = [chr(65 + i) for i in range(26)]

    words = ["Wr fhvf erfreirr pbzzrag 😹"]

    for i in range(27) :
        print(i,end="- ")
        for word in words :
            shiffer = ""
            for letter in word :
                if letter in [' ', '?', '.', '\'', '😹',','] :
                    shiffer += letter
                else :
                    shiffer += alphabet_majuscules[(alphabet_majuscules.index(letter.upper()) - i) % 26]
            print(shiffer,end=" ")
        print()

def char_to_number() :
    message = "Mais bon j'apprecie bien les filles de ton gens. Dors bien Nerys et fais de beaux reves"
    shiffer = ""
    for letter in message :
        shiffer += str(ord(letter))
        shiffer += " "
    
    print(shiffer)

def number_to_char() :
    message = "77 97 105 115 32 98 111 110 32 106 39 97 112 112 114 101 99 105 101 32 98 105 101 110 32 108 101 115 32 102 105 108 108 101 115 32 100 101 32 116 111 110 32 103 101 110 115 46 32 68 111 114 115 32 98 105 101 110 32 78 101 114 121 115 32 101 116 32 102 97 105 115 32 100 101 32 98 101 97 117 120 32 114 101 118 101 115".split()
    de_shiffer = ""
    for number in message :
        de_shiffer += chr(int(number))
    
    print(de_shiffer)

number_to_char()