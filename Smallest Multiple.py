def gcd(a,b) :
    if b == 0 :
        return a
    
    return gcd(b,a%b)

try :
    while True:
        s = list(map(int , input().split()))
        if len(s) == 0 :
            break
        if len(s) == 1 :
            print(s[0])
        else :
            a = s[0]*s[1]//gcd(max(s[0],s[1]) , min(s[0],s[1]))
            for x in range(2,len(s)) :
                a = a*s[x]//gcd(max(a,s[x]),min(a,s[x]))
            
            print(a)

except EOFError :
    pass