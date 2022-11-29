def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    l = len(digits)

    i = l - 1

    while digits[i] == 9 and i >= 0:
        i -= 1
    
    if i == -1:
        res = [0] * (l + 1)
        res[0] = 1
        return res
    
    res = [0] * (l)
    res[i] = digits[i] + 1

    for j in range(i - 1, -1, -1):
        res[j] = digits[j]
    
    return res

if __name__ == "__main__":
    lst = [1,2,9]
    print(plusOne(lst))