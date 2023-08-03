while True :
    s = input()
    if s == "0" :
        break
    else :
        s = s.replace(",",".")
        a,b,c,d,p = map(float , s.split(" "))
        a = abs(a-c)**p
        b = abs(b-d)**p
        c = (a+b)**(1/p)
        print(c)