cont = 1
res=[]
while cont == 1 :
    a,b=map(str,input().split(" "))
    if b == '0' and a == '0' :
        cont = 0
    else :
        d,r=0,0
        a,b=str(max(int(a),int(b))),str(min(int(a),int(b)))
        a,b=list(a),list(b)
        for i in range(len(a)-len(b)) :
            b.insert(0,'0')
        for i in range(len(a)) :
            if int(a[len(a)-1-i]) + int(b[len(a)-1-i]) + r > 9 :
                d+=1
                r=1
            else :
                r=0
        res.append(d)
                
for b in res :
    if b == 0 :
        print("No carry operation.")
    elif b == 1 :
        print(b,"carry operation.")
    else :
        print(b,"carry operations.")