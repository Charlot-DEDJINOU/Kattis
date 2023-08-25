for _ in range(int(input())) :
    s = list(map(int , input().split()))
    print(sum(s[1:]) + 1 - s[0])