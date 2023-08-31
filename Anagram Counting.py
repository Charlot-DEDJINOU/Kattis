from math import factorial
from collections import Counter

def count_anagrams(word):
    total_anagrams = factorial(len(word))
    letter_counts = Counter(word)
    
    for count in letter_counts.values():
        total_anagrams //= factorial(count)
        
    return total_anagrams

while True :
    try :
        s = input()
        print(count_anagrams(s))
    except EOFError :
        break
