while True :
    n = int(input())
    if n == 0 :
        break
    
    foods = dict()
    for _ in range(n) :
        s = input().split()
        for x in s[1:] :
            if x not in foods.keys() :
                foods[x] = []
            
            foods[x].append(s[0])

    foods = dict(sorted(foods.items() , key = lambda item : (item[0] , item[1])))

    for (key , value) in foods.items() :
        print(key , *sorted(value))