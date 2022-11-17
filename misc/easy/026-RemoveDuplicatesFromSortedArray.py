def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l = len(nums)
    if l < 2:
        return l
    
    pre = 0
    for current in range(1, l):
        if nums[current] != nums[pre]:
            pre += 1
            nums[pre] = nums[current]
    
    return pre + 1

if __name__ == "__main__":
    lst = [1,1,2]
    lst2 = [0,0,1,1,1,2,2,3,3,4]
    print(removeDuplicates(lst))
    print(removeDuplicates(lst2))