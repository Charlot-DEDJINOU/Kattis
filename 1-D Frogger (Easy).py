n,index,case_magic=map(int,input().split())
s=[int(x) for x in input().split()]
h=0
while True :
    if index <= 0 :
        print("left")
        break
    elif index > len(s) :
        print("right")
        break
    elif s[index-1] == 0 :
        print("cycle")
        break
    elif s[index-1] == case_magic :
        print("magic")
        break
    else :
        tmp=s[index-1]
        s[index-1]=0
        index+=tmp
        h+=1
print(h)