def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    spl = s.split()
    return len(spl[len(spl) - 1])


if __name__ == "__main__":
    s = "   fly me   to   the moon  "
    print(s, "\t -> length of last word:", lengthOfLastWord(s))
    s2 = "luffy is still joyboy"
    print(s2, "\t -> length of last word:", lengthOfLastWord(s2))