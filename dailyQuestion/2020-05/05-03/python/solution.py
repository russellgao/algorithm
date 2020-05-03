def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    m = len(nums1)
    n = len(nums2)
    # 保证n >= m
    if m > n:
        nums1, nums2 = nums2, nums1
        m, n = n, m
    half_m_n = (m + n + 1) >> 1
    imin = 0
    imax = m
    while imin <= imax:
        i = (imin + imax) >> 1
        j = half_m_n - i
        if imin < m and nums1[i] < nums2[j - 1]:
            imin = i + 1
        elif imax > 0 and nums1[i - 1] > nums2[j]:
            imax = i - 1
        else:
            # 找到复合条件的i
            if i == 0:
                max_of_left = nums2[j - 1]
            elif j == 0:
                max_of_left = nums1[i - 1]
            else:
                max_of_left = max(nums1[i - 1], nums2[j - 1])

            # 如果是奇数
            if (m + n) % 2 == 1:
                return max_of_left

            # 如果是偶数
            if i == m:
                min_of_right = nums2[j]
            elif j == n:
                min_of_right = nums1[i]
            else:
                min_of_right = min(nums1[i], nums2[i])
            return (min_of_right + max_of_left) / 2


if __name__ == "__main__" :
    nums1 = [1,2,3]
    nums2 = [3,4]
    c = findMedianSortedArrays(nums1, nums2 )
    print()