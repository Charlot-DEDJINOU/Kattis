def main():
    a, b, c, d = 0, 0, 0, 0
    tab = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    mot = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    res = input()
    
    for char in res:
        if char == '_':
            a += 1
        else:
            if char in tab:
                b += 1
            elif char in mot:
                c += 1
            else:
                d += 1
    
    total = len(res)
    print("%.15f\n%.15f\n%.15f\n%.15f" % (a/total, b/total, c/total, d/total))

if __name__ == "__main__":
    main()