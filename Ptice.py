n = int(input())
etudiants = {
    "adrian" : ['A', 'B' , 'C'] * n ,
    "bruno"  : ['B' , 'A' ,'B' , 'C'] * n ,
    "goran"  : ['C' , 'C' , 'A' , 'A' , 'B' , 'B'] * n,
}

adrian , bruno , goran = 0 , 0, 0
s = input()

for i in range(n) :
    bruno += 1 if etudiants['bruno'][i] == s[i] else 0
    adrian += 1 if etudiants['adrian'][i] == s[i] else 0
    goran += 1 if etudiants['goran'][i] == s[i] else 0

maxi = max(bruno , adrian , goran)

print(maxi)
if adrian == maxi :
    print("Adrian")
if bruno == maxi :
    print("Bruno")
if goran == maxi :
    print("Goran")
