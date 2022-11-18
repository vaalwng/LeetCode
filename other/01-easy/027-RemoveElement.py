def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    while val in nums:
        nums.remove(val)

    print(nums)

    return len(nums)


if __name__ == "__main__":
    print(removeElement([3,2,2,3], 3))
    print(removeElement([0,1,2,2,3,0,4,2], 2))