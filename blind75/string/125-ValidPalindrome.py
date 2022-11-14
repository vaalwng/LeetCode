def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    # temporary string to hold all alphabetical characters
    temp = ""

    # iterate through string
    for char in s:
        
        # append lowercase version of character to temp if and only if the character is in the alphabet
        if char.isalpha():
            temp = temp + char.lower()
    
    # return true if the temp string is equal to its reversed version, else false
    return temp == temp[::-1]
        

if __name__ == "__main__":
    s = "racecar"
    s2 = "not a-palindrome123 "
    s3 = "not a palindrome"
    print(isPalindrome(s))
    print(isPalindrome(s2))
    print(isPalindrome(s3))