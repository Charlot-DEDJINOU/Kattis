while True :
    n = int(input())
    if n == -1 :
        break

    graph = dict()
    sommets = set()
    for i in range(n) :
        s = list(map(int , input().split()))
        graph[i] = [j for j in range(n) if s[j] == 1 and i != j]

    for i in range(n) :
        if len(graph[i]) < 2 :
            continue

        for a in graph[i] :
            for b in graph[a] :
                if b in graph[i] :
                    sommets.add(i)
                    sommets.add(b)
                    sommets.add(a)

    if len(sommets) == n :
        print("")
    else :
        print(*[x for x in range(n) if x not in sommets])