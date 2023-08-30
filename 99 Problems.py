x=input()
if len(x)<3 :
    print("99")
else :
    a=x[:len(x)-2]
    b=str(int(a)-1)+"99"
    c=a+"99"
    if int(x)-int(b) < int(c)-int(x) :
        print(b if b[0]!='0' else b[1:])
    else :
        print(c)