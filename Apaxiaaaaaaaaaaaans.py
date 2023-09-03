def main():
    tab = input()
    result = ''
    
    for i in range(len(tab)-1):
        if tab[i] != tab[i+1]:
            result += tab[i]
    
    print(result + tab[-1])

if __name__ == "__main__":
    main()