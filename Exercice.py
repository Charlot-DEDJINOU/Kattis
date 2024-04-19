alphabets = [chr(x) for x in range(97, 26 + 97)]

def decrypt(message, key) :
    s = ''
    for letter in message :
        s += alphabets[(alphabets.index(letter) - key) % 26]

    return s

n, m = map(int, input().split())
s = input()
cipher = input()
key = (alphabets.index(cipher[-1]) - alphabets.index(s[-1])) % 26
print(key)
print(decrypt(cipher, key))