def main():
    n = int(input())
    tab = list(map(int , input().split()))
    mot = [x for x in tab]

    mot.sort()
    print("1", end=" ")

    for i in range(n - 1):
        for j in range(n - 1):
            if mot[i] == tab[j]:
                print(j + 2, end=" ")
                break

if __name__ == "__main__":
    main()
