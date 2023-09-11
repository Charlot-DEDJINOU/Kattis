def main():
    n = int(input())
    mots = []
    tabs = []

    for _ in range(n):
        mot, tab = input().split()
        mots.append(mot)
        tabs.append(tab)

    unique_mots = set()
    count = 0

    for i in range(n):
        if mots[i] not in unique_mots:
            unique_mots.add(mots[i])
            count += 1
            print(mots[i], tabs[i])
            if count == 12:
                break

if __name__ == "__main__":
    main()