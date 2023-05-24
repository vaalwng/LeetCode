def isPalindromeNumber(x):
    """
    :type x: int
    :rtype: bool
    """
    # if number is negative return false
    if x < 0:
        return False

    # store input since we will be manipulating it
    num = x
    # variable to hold the reversed number
    reverse = 0

    # reverse the integer
    while num:
        reverse = reverse * 10 + num % 10
        num //= 10
    
    # compare the original to its reversed
    return x == reverse

if __name__ == "__main__":
    print(isPalindromeNumber(123))
    print(isPalindromeNumber(-121))
    print(isPalindromeNumber(10))