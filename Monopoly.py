def fill() :
    univers = dict() 
    for i in range(1,7) :
        for j in range(1,7) :
            if i + j not in univers.keys() :
                univers[i+j] = [(i,j)]
            elif (i,j) not in univers[i+j] :
                univers[i+j].append((i,j))

    return univers

n = int(input())
univers = fill()
print(sum([(len(univers[x]) / 36) for x in list(map(int , input().split()))]))
