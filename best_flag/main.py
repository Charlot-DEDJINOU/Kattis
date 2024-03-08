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


crypte(5)
shiffer(9)
deshiffer(9)
decrypte(5)