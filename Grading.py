sign = ['A','B','C','D','E','F']
n = list(map(int,input().split()))
n.append(0)
note = int(input())
for i in range(6) :
    if note >= n[i] :
        print(sign[i])
        break