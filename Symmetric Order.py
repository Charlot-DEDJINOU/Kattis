number = 0

while True:
    n = int(input())
    if n == 0:
        break

    number += 1
    sup = []
    inf = []

    for i in range(n):
        entry = input()
        if i % 2 == 0:
            sup.append(entry)
        else:
            inf.append(entry)

    print("SET", number)
    for x in sup:
        print(x)
    for x in reversed(inf):
        print(x)
