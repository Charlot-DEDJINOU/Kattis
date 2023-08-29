n = int(input())
d , start = 0 , 0
for i in range(n) :
    if i % 2 == 1 :
        d += int(input()) - start
    else :
        start = int(input())

print(d if n % 2 == 0 else "still running")