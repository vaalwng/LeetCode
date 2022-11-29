def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    # Newton's method
    # result = x
    # while not result * result - x < 1:
    #     result = (result + x / result) / 2
    
    # return int(result)

    # Binary search method
    # find largest in whose square is less or equal than x
    left, right = 0, x
    while left <= right:
        mid = left + (right - left) // 2

        if mid * mid > x:
            right = mid -1
        elif mid * mid < x:
            left = mid + 1
        else:
            return mid
    
    # left > right
    return right

if __name__ == "__main__":
    print(mySqrt(144))
    print(mySqrt(4))
    print(mySqrt(8))
