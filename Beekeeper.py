voyelles = ['a' , 'e' , 'i' , 'o' , 'u' , 'y']

while True :
    n = int(input())

    if n == 0 :
        break

    textes = dict()
    index = 0
    maxi = 0

    for i in range(n) :
        total = 0
        s = input()
        textes[i] = s
        for voyelle in voyelles :
            double = voyelle + voyelle
            total += s.count(double)
        
        if total > maxi :
            maxi = total
            index = i

    print(textes[index])