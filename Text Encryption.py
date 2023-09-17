while True :
    n = int(input())
    if n == 0 :
        break
    
    s = input().replace(' ' , '')
   
    if len(s) > n :
        nextLetter = 0
        nextPlace = 0
        count = 0
        
        res = [""] * len(s)
        if len(s) > n:
                while count < n:
                    res[nextPlace] = s[nextLetter].upper()
                    nextLetter += 1
                    nextPlace += n
                    if nextPlace >= len(s) or nextLetter >= len(s):
                            count += 1
                            nextPlace = count
        print(''.join(res))
    else :
        print(s.upper())