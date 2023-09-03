def main():
    tab = list(map(int, input().split()))
    mot = input()

    min_value = min(tab)
    max_value = max(tab)

    for num in tab:
        if num != min_value and num != max_value:
            in_value = num

    if mot == "ABC":
        print(min_value, in_value, max_value)
    elif mot == "BAC":
        print(in_value, min_value, max_value)
    elif mot == "ACB":
        print(min_value, max_value, in_value)
    elif mot == "BCA":
        print(in_value, max_value, min_value)
    elif mot == "CAB":
        print(max_value, min_value, in_value)
    else:
        print(max_value, in_value, min_value)

if __name__ == "__main__":
    main()