def find_inverse(num, modulus):
    for i in range(1, modulus):
        if num * i % modulus == 1:
            return i
    return 0

def convert_to_char_or_digit(value):
    if 1 <= value <= 26:
        return chr(64 + value)
    elif 27 <= value <= 36:
        return str(value - 27)
    else:
        return '_'

def main():
    numbers = list(map(int, input().split()))
    result = ''

    for num in numbers:
        inverse = find_inverse(num, 41)
        result += convert_to_char_or_digit(inverse)

    print(result)

if __name__ == "__main__":
    main()