def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    # 2-Pass approach
    l = len(nums)

    if len == 0 or nums is None:
        return nums
    
    ans = [1] * l

    for i in range(1, l):
        ans[i] = nums[i-1] * ans[i-1]

    right = 1

    for i in range(l - 1, -1, -1 ):
        ans[i] *= right
        right *= nums[i]
    
    return ans

if __name__ == "__main__":
    arr = [1,2,3,4]
    print(productExceptSelf(arr))
