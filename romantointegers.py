s = 'VIII'

roman_symbols = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

result = 0

for i in range(len(s)):
    if i+1 != len(s) and roman_symbols[s[i]] < roman_symbols[s[i+1]]:
        result = result - roman_symbols[s[i]]
    else:
        result = result + roman_symbols[s[i]]

print(result)