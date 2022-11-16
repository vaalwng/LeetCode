def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    results = [0]

    for i in range(1, n + 1):
        results.append(results[i & (i-1)] + 1)
    
    return results

if __name__ == "__main__":
    print(countBits(2))
    print(countBits(5))
