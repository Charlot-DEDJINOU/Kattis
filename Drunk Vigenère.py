def main():
    res = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    tab = input()
    mot = input()
    result = ''

    for i in range(len(tab)):
        a = res.index(tab[i])
        b = res.index(mot[i])

        if (i + 1) % 2 == 0:
            result += res[(a + b) % 26]
        elif a - b < 0:
            result += res[a - b + 26]
        else:
            result += res[a - b]

    print(result)

if __name__ == "__main__":
    main()