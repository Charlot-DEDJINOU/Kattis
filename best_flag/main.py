import math

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def write_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)

    except Exception as e:
        print(f"Error: {e}")

def crypte(key) :
    messages = read_file('example.txt').split(chr(10))
    content = list()
    for message in messages :
        shiffer = ' '.join([str(ord(c) + key) for c in message])
        content.append(shiffer)

    write_file('shiffer1.txt', chr(10).join(content))

def shiffer(key) :
    messages = read_file('shiffer1.txt').split(chr(10))
    content = list()
    for message in messages :
        for c in message.split() :
            content.append(chr(32) * int(c) + chr(key))
        
        content.append(chr(10))
    
    content.pop()

    write_file('shiffer2.txt', ''.join(content))


def deshiffer(key) :
    messages = read_file('shiffer2.txt').split(chr(10))
    content = list()
    for message in messages :
        deshiffer = ' '.join([str(len(c)) for c in message.split(chr(key))[:-1]])
        content.append(deshiffer)

    write_file('deshiffer2.txt', chr(10).join(content))
    
def decrypte(key) :
    messages = read_file('deshiffer2.txt').split(chr(10))
    content = list()
    for message in messages:
        deshiffer = ''.join([chr(int(c) - key) for c in message.split()])
        content.append(deshiffer)

    write_file('deshiffer1.txt', chr(10).join(content))

def textEncryption(key, s) : 

    if len(s) > key :
        nextLetter = 0
        nextPlace = 0
        count = 0
        
        res = [""] * len(s)
        if len(s) > key:
                while count < key:
                    res[nextPlace] = s[nextLetter].upper()
                    nextLetter += 1
                    nextPlace += key
                    if nextPlace >= len(s) or nextLetter >= len(s):
                            count += 1
                            nextPlace = count
        return ''.join(res)
    else :
        return s.upper()

def textDecryption(key, ciphertext):
    if len(ciphertext) > key:
        columns = len(ciphertext) // key
        rows = math.ceil(len(ciphertext) / key)
        empty_cells = (rows * columns) - len(ciphertext)
        plaintext = [''] * rows
        current_row, current_col = 0, 0
        for char in ciphertext:
            plaintext[current_row] += char
            current_col += 1
            if (current_row == rows - 1) or (current_col == columns and current_row >= rows - empty_cells):
                current_col = 0
                current_row += 1
        return ''.join(plaintext)
    else:
        return ciphertext.upper()

# Example usage
key = 4
text = "Nerys"
text_encrypted = textEncryption(key, text)
decrypted_text = textDecryption(key, text_encrypted)
print(text_encrypted,decrypted_text)