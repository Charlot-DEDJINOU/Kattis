alphabets = [chr(i + 65) for i in range(26)]
number = [int(x) for x in input()]
n = int(input())
for _ in range(n) :
    s = input()
    shiffer = ""
    for (index ,letter) in enumerate(s) :
        shiffer += alphabets[(alphabets.index(letter) * number[index]) % 26]

    print(shiffer)