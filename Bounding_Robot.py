while True :
    think = [0,0]
    actually = [0,0]
    w , l = map(int , input().split())
    if w == l == 0 :
        break

    tour = int(input())
    for x in range(tour) :
        s = input().split()
        if s[0] == "u" :
            think[1] += int(s[1])
            if actually[1] + int(s[1]) >= l :
                actually[1] = l - 1
            else :
                actually[1] += int(s[1])
        if s[0] == "d" :
            think[1] -= int(s[1])
            if actually[1] - int(s[1]) < 0 :
                actually[1] = 0
            else :
                actually[1] -= int(s[1])
        if s[0] == "l" :
            think[0] -= int(s[1])
            if actually[0] - int(s[1]) < 0 :
                actually[0] = 0
            else :
                actually[0] -= int(s[1])
        if s[0] == "r" :
            think[0] += int(s[1])
            if actually[0] + int(s[1]) >= w :
                actually[0] = w - 1
            else :
                actually[0] += int(s[1])
    print("Robot thinks",think[0],think[1],end="\n")
    print("Actually at",actually[0],actually[1],end="\n")