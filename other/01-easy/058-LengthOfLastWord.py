def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    spl = s.split()
    return len(spl[len(spl) - 1])


if __name__ == "__main__":
    s = "   fly me   to   the moon  "
    print(lengthOfLastWord(s))
    s2 = "luffy is still joyboy"
    print(lengthOfLastWord(s2))