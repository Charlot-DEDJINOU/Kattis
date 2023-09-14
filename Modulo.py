def main():
    tab = []
    
    for i in range(10):
        num = int(input()) % 42
        if num not in tab :
            tab.append(num)
            
    print(len(tab))

if __name__ == "__main__":
    main()
