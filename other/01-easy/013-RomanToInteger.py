def romanToInteger(s):
    """
    :type s:str
    :rtype: int
    """
    # roman numeral mappings
    numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    # lenth of string
    l = len(s)

    # stores result
    num = numerals[s[l-1]]

    # iterate from right to left
    for i in range(l - 2, -1, -1):
        # identify if char at right of current char is bigger or smaller
        if numerals[s[i]] >= numerals[s[i+1]]:
            num += numerals[s[i]]
        else:
            num -= numerals[s[i]]
    
    return num
    
if __name__ == "__main__":
    print(romanToInteger("MCMXCIV"))