def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    a, b = list(a), list(b)
    carry = 0
    ans = ""

    while a or b or carry:
        if a:
            carry += int(a.pop())
        if b:
            carry += int(b.pop())
        carry, remain = divmod(carry, 2)
        ans = str(remain) + ans
    
    return ans

if __name__ == "__main__":
    a = "1010"
    b = "1011"
    print(addBinary(a, b))