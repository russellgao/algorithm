def searchInsert(nums: [int], target: int) -> int:
    left ,right = 0 , len(nums) - 1
    while left <= right :
        mid = (left + right) >> 1
        if nums[mid] == target :
            return mid
        if nums[mid] > target :
            right = mid -1
        else :
            left = mid + 1
    return left


if __name__ == "__main__" :
    nums = [1,3,5,6]
    target = 2
    result = searchInsert(nums,target)
    print(result)