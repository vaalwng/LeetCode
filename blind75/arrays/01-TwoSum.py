def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    # NOTE: minuend - subtrahend = difference

    # instantiate empty dictionary 
    required = {}
    
    # iterate through the nums array
    for i in range(len(nums)):

        # based on the current number/element if found the minuend in the dictionary
        # return the indexes of that from the dictionary, and the current element index
        if target - nums[i] in required:
            return [required[target - nums[i]],i]
        
        # add the minuend and its index to the dictionary
        else:
            required[nums[i]] = i
    
    # if unable to find, return null
    return None

if __name__ == "__main__":
    n = [2, 7, 11, 15]
    t = 18
    print("twoSum( array:", n, ", target:", t, ") -->", twoSum(n, t))