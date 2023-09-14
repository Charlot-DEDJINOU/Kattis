n = int(input())
matrix = [[0]*3 for i in range(n)]
for i in range(3) :
    s = list(map(int , input().split()))
    for j in range(n) :
        matrix[j][i] = s[j]

for x in matrix :
    print(sorted(x)[1] , end=" ")