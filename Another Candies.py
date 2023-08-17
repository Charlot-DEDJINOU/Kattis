t = int(input())

for _ in range(t) :
    n = input()
    bonbons = 0
    n = int(input())
    for i in range(n) :
        bonbons += int(input())

    answer = "YES" if bonbons % n == 0 else "NO"
    print(answer)