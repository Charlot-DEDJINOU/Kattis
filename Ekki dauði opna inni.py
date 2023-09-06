s = input().split('|')
r = input().split('|')

for i in range(max(len(s) , len(r))) :
    if i < len(s) :
        print(s[i] , end="")
    if i < len(r) :
        print(r[i] , end=" ")