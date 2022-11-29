def minFlips(target):
    """
    :type target: str
    :rtype: int
    """
    curr = '1'
    count = 0

    for i in range(len(target)):

        # if curr occurs in the final string
        if target[i] == curr:
            count += 1

            # switch curr to '0' if '1'
            # or vice versa
            curr = chr(48 + (ord(curr) + 1) % 2)
    
    return count


if __name__ == "__main__":
    s = "01011"
    print(minFlips(s))