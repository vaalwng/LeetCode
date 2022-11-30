def uniqueOccurrences(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    # approach: count occurences and check if numbers of occurrences are the same
    
    # create a dictionary to hold number of occurences
    visited = {}

    for n in arr:
        visited[n] = visited.get(n, 0) + 1

    print("visited:", visited)

    values = set()
    for key, value in visited.items():
        if value in values:
            return False
        values.add(value)
    
    return True
    
    

if __name__ == "__main__":
    arr = [1,2,2,1,1,3]
    print(uniqueOccurrences(arr))
    # arr2 = [1,2]
    # print(uniqueOccurrences(arr2))
    # arr3 = [-3,0,1,-3,1,1,1,-3,10,0]
    # print(uniqueOccurrences(arr3))