n , q  = map(int , input().split())
money = dict()
restart = 0

for _ in range(q) :
    s = input().split()
    if s[0] == "SET" :
        money[s[1]] = s[2]
    elif s[0] == "RESTART" :
        restart = s[1]
        money.clear()
    else :
        if s[1] in money.keys() :
            print(money[s[1]])
        else :
            print(restart)