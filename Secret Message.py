def carre(n) :
    i = 1 
    while i**2 < n :
        i +=1
        
    return i

n = int(input())

for _ in range(n) :
    s = input()
    k = carre(len(s))
    s += '*'*(k*k-len(s))
    s = [x for x in s]
    message = [[0] * k for _ in range(k)]
    for i in range(k) :
        for j in range(k) :
            message[j][k-i-1] = s[k*i+j]

    print(*[x for m in message for x in m if x != '*'],sep="")
