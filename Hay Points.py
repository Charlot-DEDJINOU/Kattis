m , n = map(int , input().split())
jobs = dict()
for _ in range(m) :
    a , b = input().split()
    jobs[a] = int(b)

for _ in range(n) :
    total = 0
    while True :
        s = input()
        if s == "." :
            break

        s = s.split()
        for x in s :
            if x in jobs.keys() :
                total += jobs[x]

    print(total)