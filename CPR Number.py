def main():
    mot = input()
    s = 0

    for i in range(11):
        if i == 0:
            s += int(mot[i]) * 4
        elif i == 1:
            s += int(mot[i]) * 3
        elif i == 2:
            s += int(mot[i]) * 2
        elif i == 3:
            s += int(mot[i]) * 7
        elif i == 4:
            s += int(mot[i]) * 6
        elif i == 5:
            s += int(mot[i]) * 5
        elif i == 7:
            s += int(mot[i]) * 4
        elif i == 8:
            s += int(mot[i]) * 3
        elif i == 9:
            s += int(mot[i]) * 2
        elif i == 10:
            s += int(mot[i]) * 1

    if s % 11 == 0:
        print("1")
    else:
        print("0")

if __name__ == "__main__":
    main()
