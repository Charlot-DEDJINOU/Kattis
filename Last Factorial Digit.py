def fact(n) :
    if n == 0 or n == 1 :
        return 1
    return n*fact(n-1)

for _ in range(int(input())) :
    print(str(fact(int(input())))[-1])