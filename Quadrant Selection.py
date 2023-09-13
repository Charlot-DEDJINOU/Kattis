def main():
    n, r = int(input()) , int(input())
    if n > 0 and r > 0:
        print("1")
    elif n > 0 and r < 0:
        print("4")
    elif n < 0 and r < 0:
        print("3")
    elif n < 0 and r > 0:
        print("2")

if __name__ == "__main__":
    main()