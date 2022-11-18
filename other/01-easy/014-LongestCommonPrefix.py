def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype str
    """
    if len(strs) == 0:
        return None
    if len(strs) == 1:
        return strs[0]
    
    n = len(strs[0])
    for i in range(1, len(strs)):
        n = min(n, len(strs[i]))
        while n > 0 and strs[0][0:n] != strs[i][0:n]:
            n -= 1
        if n == 0:
            return ""
        
    return strs[0][0:n]


if __name__ == "__main__":
    l1 = ["flower","flow","flight"]
    l2 = ["dog","racecar","car"]
    l3 = ["dog","do","done"]
    print(longestCommonPrefix(l1))
    print(longestCommonPrefix(l2))
    print(longestCommonPrefix(l3))