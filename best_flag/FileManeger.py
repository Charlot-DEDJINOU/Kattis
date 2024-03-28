def read(filename):
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

def write(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)

    except Exception as e:
        print(f"Error: {e}")