def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if s == "":
        return 0
    
    # sliding window approach
    start = 0
    end = 0

    # tracker for the largest length ofvalid subtring
    maxLength = 0
    unique_chars = set()
    
    # iterate through the entire string
    while end < len(s):

        # if current char is not in the set, add it
        if s[end] not in unique_chars:
            unique_chars.add(s[end])
            end += 1
            maxLength = max(maxLength, len(unique_chars))
        # if the current char is present in the set, remove it
        # then change the start index of the sliding window
        else:
            unique_chars.remove(s[start])
            start += 1   

    # return the largest value length
    return maxLength

if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcabcbb"))