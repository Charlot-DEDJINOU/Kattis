for _ in range(int(input())) :
    villes = {}
    for i in range(int(input())) :
        ville = input()
        if ville in villes.keys() :
            villes[ville] +=1
        else :
            villes[ville] = 0
    
    print(len(villes))