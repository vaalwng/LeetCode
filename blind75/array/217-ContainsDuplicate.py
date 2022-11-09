def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """

    # create a set
    d = set()

    # iterate through the array
    for n in nums:
        # if the current element is present in the set return True
        if n in d:
            return True
        # otherwise, add the new element to the set
        else:
            d.add(n)

    return False

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,6,7]
    print("containsDuplicate(", "Array:", arr, ") -->", containsDuplicate(arr))    