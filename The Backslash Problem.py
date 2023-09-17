try :
    while True :
        n = int(input())
        s = input()
        for i in range(n) :
            new_s = ""
            for x in s :
                if ord('!') <= ord(x) <= ord('*') or ord('[') <= ord(x) <= ord(']') :
                   new_s += '\\'

                new_s += x
            s = new_s
        print(s)
except EOFError :
    pass