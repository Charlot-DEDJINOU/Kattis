import ROTN
import Offset
import AES
import ASCII
import Substitution

# ROTN.crypt('example.txt', 'example.txt', 7, 'azertyuiopqsdfghjklmwxcvbn')
# Offset.crypt('example.txt', 'example.txt', 3)
# AES.crypt('example.txt', 'example.txt', b'FIkLjhkiZISzezeWsHbIzrNZ0hRhEOPlt8lA9R3lWuo=')
# ASCII.crypt('example.txt', 'example.txt', 5)
# Substitution.crypt('example.txt', 'example.txt', 9)

ROTN.decrypt('example.txt', 'example.txt', 7, 'azertyuiopqsdfghjklmwxcvbn')