for _ in range(int(input())) :
    index, n = map(int, input().split())

    print(index, n * (n + 1) //2, n * (1 + (n-1)*2 + 1) //2, n * (2 + (n-1)*2 + 2) //2)