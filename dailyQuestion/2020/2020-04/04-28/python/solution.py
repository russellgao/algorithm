# 解决方法
# 采用二分法进行解答
# 数组本身不是有序的，进行旋转后只保证了数组的局部是有序的
# 在常规二分搜索的时候查看当前 mid 为分割位置分割出来的两个部分 [l, mid] 和 [mid + 1, r] 哪个部分是有序的，并根据有序的那个部分确定我们该如何改变二分搜索的上下界，因为我们能够根据有序的那部分判断出 target 在不在这个部分：

# 如果 [l, mid - 1] 是有序数组，且 target 的大小满足 [\textit{nums}[l],\textit{nums}[mid])[nums[l],nums[mid])，则我们应该将搜索范围缩小至 [l, mid - 1]，否则在 [mid + 1, r] 中寻找。
# 如果 [mid, r] 是有序数组，且 target 的大小满足 (\textit{nums}[mid+1],\textit{nums}[r]](nums[mid+1],nums[r]]，则我们应该将搜索范围缩小至 [mid + 1, r]，否则在 [l, mid - 1] 中寻找。


def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if not nums :
        return -1
    left = 0
    right = len(nums) - 1
    while left <= right :
        mid = (left + right) >> 1
        if nums[mid] == target :
            return mid
        if nums[0] <= nums[mid] :
            if nums[0] <= target < nums[mid] :
                right = mid - 1
            else :
                left = mid + 1
        else :
            if nums[mid] < target <= nums[len(nums) - 1] :
                left = mid + 1
            else :
                right = mid -1
    return -1

# 时间复杂度： O(\log n)O(logn)，其中 nn 为 \textit{nums}[]nums[] 数组的大小。整个算法时间复杂度即为二分搜索的时间复杂度 O(\log n)O(logn)。
#
# 空间复杂度： O(1)O(1) 。我们只需要常数级别的空间存放变量。
