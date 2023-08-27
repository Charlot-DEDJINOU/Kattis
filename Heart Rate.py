for _ in range(int(input())) :
    b , p = map(float , input().split())
    b = int(b)
    p = 60/p
    print(*["{:.4f}".format(i*p) for i in range(b-1,b+2)])