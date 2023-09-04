def main():
    tab = []
    
    for i , a in enumerate(list(map(int , input().split()))) :
        if i == 0 or i == 1:
            tab.append(1 - a)
        elif i == 2 or i == 3 or i == 4:
            tab.append(2 - a)
        else:
            tab.append(8 - a)
    
    print(" ".join(map(str, tab)))

if __name__ == "__main__":
    main()