cont = 1
res=[]
while cont == 1 :
    a,b=map(int , input().split(" "))
    if a == 0 and b == 0 :
        cont = 0 
    else :
        if a+b == 13 :
            res.append(0)
        elif a == b :
            res.append(1)
        elif a > b :
            res.append(2)
        else :
           res.append(4)

for r in res :
    if r == 0 :
        print("Never speak again.")
    elif r == 1 :
        print("Undecided.")
    elif r == 2 :
        print("To the convention.")
    else :
        print("Left beehind.")