def number_to_words(n):
    try :
        n = int(n) 
        if 0 <= n <= 20:
            return ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                    "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty"][n]
        elif 20 < n <= 99:
            word = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"][n // 10]
            if number_to_words(n % 10) != "Zero" :
                word += ("-" + number_to_words(n % 10)).rstrip().lower()

            return word
    except :
        return n

try :
    while True :
        n = input().split()
        res = ""
        for x in n :
            res += number_to_words(x) + " "
        res = res.capitalize()
        print(res)

except EOFError :
    pass