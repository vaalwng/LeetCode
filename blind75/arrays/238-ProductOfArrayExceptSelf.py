def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    # 2-Pass approach
    l = len(nums)
    if len == 0 or nums is None:
        return nums
    
    # declare an empty array with 1s with length of given array
    ans = [1] * l

    # left
    for i in range(1, l):
        ans[i] = nums[i-1] * ans[i-1]
        print(i, ans)    

    print("")
    # right
    right = 1
    for i in range(l - 1, -1, -1 ):
        ans[i] *= right
        right *= nums[i]
        print(i, ans)    
    
    return ans

    # ===============================

    # 1-Pass approach

    # # declare left and right products
    # left = 1
    # right = 1

    # # declare len variable for the sake of convenience
    # l = len(nums)

    # # handle an empty array
    # if l == 0 or nums is None:
    #     return nums
    
    # # declare an empty array with 1s with length of given array
    # ans = [1] * l

    # # iterate through the array
    # for i in range(0, l):
    #     # left
    #     ans[i] *= left
    #     left *= nums[i]

    #     # right
    #     ans[l-i-1] *= right
    #     right *= nums[l-i-1]

    #     print(i, l-i-1, ans)
    
    # return ans


if __name__ == "__main__":
    arr = [1,2,3,4]
    productExceptSelf(arr)
    # print(productExceptSelf(arr))

    # arr2 = [-1,1,0,-3,3]
    # print(productExceptSelf(arr2))
