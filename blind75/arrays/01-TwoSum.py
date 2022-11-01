def TwoSum(nums, target):
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
        # if found the minuend, return the indexes
        if target - nums[i] in required:
            return [required[target - nums[i]],i]
        # for each element find the subtrahend 
        else:
            required[nums[i]] = i
    
    # if unable to find, return null
    return None

if __name__ == "__main__":
    n = [2, 7, 11, 15]
    t = 3
    print(TwoSum(n, t))