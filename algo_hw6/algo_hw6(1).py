def merge_two_sorted_arrays(nums1, m, nums2, n):
    while None in nums1:
        nums1.pop()
    for i in nums2:
        nums1.append(i)
    nums1.sort()
    return nums1[:m+n]