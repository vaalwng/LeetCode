def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    # if the given string don't have the same length, already not an anagram
    if len(s) != len(t):
        return False

    # loop through the each element of the set of the first string and compare counts of the two strings
    for element in set(s):
        if s.count(element) != t.count(element):
            return False
    
    return True
    
if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s, t))

    s2 = "youtube"
    t2 = "twitch"
    print(isAnagram(s2, t2))