for _ in range(int(input())) :
    s = input().split('+')
    print("skipped" if s[0] == "P=NP" else int(s[0])+int(s[1]))