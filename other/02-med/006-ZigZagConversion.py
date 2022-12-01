def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if s is None and numRows <= 0:
        return ""
    if numRows == 1:
        return s 
    
    result = ""

    step = 2 * numRows - 2

    for i in range(0, numRows):
        for j in range(i, len(s), step):
            result += s[j]
            if i != 0 and i != numRows - 1 and (j + step - 2 * i) < len(s):
                result += s[j + step - 2 * i]
    
    return result

if __name__ == "__main__":
    print(convert("PAYPALISHIRING", 3))