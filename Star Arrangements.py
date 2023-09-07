def vef(i,n) :
    to=0 
    j = 0
    while to < n :
        if j % 2 == 0 :
            to+=i+1
        else :
            to+=i
        j+=1

    return to == n

n=int(input())
print(n,end=":")
print("")
for i in range(1,n//2+1) :
    if n%i==0 and i !=1 :
        print(i,i,sep=",")
    if vef(i,n) == True :
        print(i+1,i,sep=",")