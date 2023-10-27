translator = dict()

while True :
    s = input()
    if s == "" :
        break

    s = s.split(" ")
    translator[s[1]] = s[0]


while True :
    try :
        s = input() 
        if s in translator.keys() :
            print(translator[s])
        else :
            print("eh")
    except EOFError :
        break