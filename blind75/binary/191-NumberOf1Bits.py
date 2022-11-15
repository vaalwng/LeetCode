def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    count = 0

    while n:
        n &= n - 1
        count += 1

    return count

if __name__ == "__main__":
    print(hammingWeight(0o11111111111111111111111111111101))