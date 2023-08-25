for _ in range(int(input())) :
    s = input().split()
    signe = 1 if s[0] == "F" else -1
    minutes = signe*int(s[1]) + int(s[2]) * 60 + int(s[3])
    heure = (minutes//60) % 24
    heure = 23 if heure == -1 else heure
    minutes = minutes % 60
    print(heure , minutes)