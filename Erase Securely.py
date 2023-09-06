def main():
    n = int(input())
    tab = input()
    mot = input()

    for _ in range(n):
        tab = ''.join(['1' if char == '0' else '0' for char in tab])

    if tab == mot:
        print("Deletion succeeded")
    else:
        print("Deletion failed")

if __name__ == "__main__":
    main()