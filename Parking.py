for _ in range(int(input())) :
    n = input()
    n = list(map(int , input().split()))
    print((max(n) - min(n))*2)