

# 二分法求解

def findDuplicate(nums: [int]) -> int :
    n = len(nums)
    left , right = 1, n-1
    result = -1
    while left <= right :
        mid = (left+right) >> 1
        cnt = 0
        for i in range(n) :
            if nums[i] <= mid :
                cnt += 1
        if cnt <= mid :
            left = mid + 1
        else :
            right = mid -1
            result = mid
    return result


if __name__ == "__main__" :
    nums = [1,3,4,2,2]
    result = findDuplicate(nums)
    print(result)

