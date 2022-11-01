def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """

    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m = len(nums1)
    n = len(nums2)

    start = 0
    end = m

    # binary search
    while start<= end:
        partition_nums1 = (start + end) // 2
        partition_nums2 = (m + n + 1) // 2 - partition_nums1

if __name__ == "__main__":
    print("abcabcbb")