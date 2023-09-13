victory = {
    "Province" : [8 , 6] ,
    "Duchy" : [5 , 3] ,
    "Estate" : [2 , 1]
}

tresuare = {
    "Gold" : [6 , 3] ,
    "Silver" : [3 , 2] ,
    "Copper" : [0 , 1]
}

tab = ["Gold" , "Silver" , "Copper"]
somme = 0

for index , value in enumerate(list(map(int ,input().split()))) :
    somme += tresuare[tab[index]][1] * value

def carte(somme , dict) :
    for key , value in dict.items() :
        if somme >= value[0] :
            return key

if carte(somme , victory) :
    print(carte(somme , victory),"or",carte(somme , tresuare))
else :
    print(carte(somme , tresuare))