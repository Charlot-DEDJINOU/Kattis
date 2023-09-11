a,b=map(int,input().split())
l=input().split(" ")
s=[]
for i in range(1,b+1) :
    s.append(l.count(str(i)))

l=[x for x in s if x == min(s)]
print(len(l))
for i in range(len(s)) :
    if s[i] == min(s) :
        print(i+1,end=" ")