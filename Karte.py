P = []
K = []
H = []
T = []
value = False

s = input()

for i in range(0,len(s)-1,3) :
    a = s[i+1:i+3]
    if(s[i] == 'P') :
        if P.count(a) != 0 :
            value = True
            break
        else :
            P.append(a)
    elif(s[i] == 'K') :
        if K.count(a) != 0 :
            value = True
            break
        else :
            K.append(a)
    elif(s[i] == 'H') :
        if H.count(a) != 0 :
            value = True
            break
        else :
            H.append(a)
    else :
        if T.count(a) != 0 :
            value = True
            break
        else :
            T.append(a)

if value == True :
    print("GRESKA")
else: 
    print(13-len(P) , 13-len(K) , 13-len(H) , 13-len(T) , sep=" ")
