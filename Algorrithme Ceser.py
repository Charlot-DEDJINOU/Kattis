alphabet_majuscules = [chr(65 + i) for i in range(26)]

print(alphabet_majuscules)
words = ["NADDSYW", "YWFLDW", "YSLZWJ" ,"WNAD"]

for i in range(27) :
    print(i,end="- ")
    for word in words :
        shiffer = ""
        for letter in word :
            shiffer += alphabet_majuscules[(alphabet_majuscules.index(letter) - i) % 26]
        print(shiffer,end=" ")
    print()