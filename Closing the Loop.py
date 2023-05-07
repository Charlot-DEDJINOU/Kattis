number_test = int(input())

for _ in range(number_test) :
    number_segment = int(input())
    longeurs = input().split(" ")
    if number_segment == 1 :
        print("Case #",_ + 1,": ",0,sep="")
    else :
        rouge = []
        bleu = []
        boucle = []
        for longeur in longeurs :
            if longeur[-1] == 'B' :
                bleu.append(int(longeur[:-1]))
            elif longeur[-1] == 'R' :
                rouge.append(int(longeur[:-1]))
        
        if len(rouge) == 0 or len(bleu) == 0 :
            print("Case #",_ + 1,": ",0,sep="")
        else :

            while True :
                if len(boucle) % 2 != 0 and len(rouge) != 0 :
                    boucle.append(max(rouge))
                    rouge.remove(max(rouge))
                elif len(boucle) % 2 == 0 and len(bleu) != 0 :
                    boucle.append(max(bleu))
                    bleu.remove(max(bleu))
                else :
                    break

            if len(boucle) % 2 != 0 :
                boucle.remove(boucle[-1])
            
            print("Case #",_ + 1,": ",sum(boucle) - len(boucle),sep="")