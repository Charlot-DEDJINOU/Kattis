def main():
    p, jour = map(int, input().split())
    mots = []

    for i in range(jour):
        mot = input()
        if mot not in mots:
            mots.append(mot)
        if len(mots) == p:
            print(i + 1)
            return
    
    print("paradox avoided")

if __name__ == "__main__":
    main()
