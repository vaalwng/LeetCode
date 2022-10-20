def TwoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    # empty dictionary 
    required = {}
    
    for i in range(len(nums)):
        if target - nums[i] in required:
            return [required[target - nums[i]],i]
        else:
            required[nums[i]]=i


if __name__ == "__main__":
    n = [2, 7, 11, 15]
    t = 9
    print(TwoSum(n, t))