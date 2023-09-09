while True:
    n = int(input())
    if n == -1:
        break
    
    total = 0
    mot = []
    
    for i in range(n):
        a, b = map(int, input().split())
        mot.append((a, b))
        if i == 0:
            total += a * b
        else:
            total += a * (b - mot[i-1][1])
    
    print(total,"miles")