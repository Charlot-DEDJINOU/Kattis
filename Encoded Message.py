for _ in range(int(input())) :
    s = input()
    c = int(len(s)**0.5)
    for i in range(c) :
        for j in range(c) :
            print(s[c*j+(c-i-1)],end="")
    print()