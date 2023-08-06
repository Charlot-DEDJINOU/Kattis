while True :
    a,b = map(int,input().split())
    if a == 0 and b == 0 :
        break
    else :
        d = 0
        if a >= b :
            d = a//b
            a = a%b
        
        print(d,a,'/',b,sep=" ")
        