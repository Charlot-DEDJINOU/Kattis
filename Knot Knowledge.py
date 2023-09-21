def main():
    n = int(input())
    mot = list(map(int, input().split()))
    tab = list(map(int, input().split()))

    for i in range(n):
        found = False
        for j in range(n - 1):
            if mot[i] == tab[j]:
                found = True
                break
        if not found:
            print(mot[i])
            break

if __name__ == "__main__":
    main()
