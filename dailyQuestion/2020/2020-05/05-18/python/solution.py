# 动态规划求解
def maxProduct(nums: [int]) -> int:
    max_nums = nums[0]
    min_nums = nums[0]
    result = nums[0]
    for i in range(1, len(nums)):
        tmp_max = max_nums
        tmp_min = min_nums
        max_nums = max(nums[i], nums[i] * tmp_max, nums[i] * tmp_min)
        min_nums = min(nums[i], nums[i] * tmp_max, nums[i] * tmp_min)
        if max_nums > result:
            result = max_nums
    return result


# 暴力求解
def maxProduct2(nums: [int]) -> int:
    result = float('-inf')
    for i in range(len(nums)):
        tmp = 1
        for j in range(i, -1, -1):
            tmp *= nums[j]
            if tmp > result:
                result = tmp
    return result


if __name__ == "__main__" :
    nums = [2,0,3,-2,3,4,4,5,5]
    result = maxProduct(nums)
    print(result)