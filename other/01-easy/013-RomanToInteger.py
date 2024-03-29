def romanToInteger(s):
    """
    :type s:str
    :rtype: int
    """
    # roman numeral mappings
    numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    # length of string
    l = len(s)

    # stores result, start with the value of the last char
    num = numerals[s[l-1]]

    # iterate from right to left
    # note: range(start_value, stop_value (exclusive), step_value)
    for i in range(l - 2, -1, -1):
        # identify if char at right of current char is bigger or smaller
        if numerals[s[i]] >= numerals[s[i+1]]: # if current is bigger or equal to the char at right
            num += numerals[s[i]]
        else:
            num -= numerals[s[i]]                
    return num
    
if __name__ == "__main__":
    print(romanToInteger("III"))
    print(romanToInteger("LVIII"))
    print(romanToInteger("MCMXCIV"))