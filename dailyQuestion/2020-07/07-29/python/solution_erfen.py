
# 二分法
def missingNumber(nums: [int]) -> int:
    i, j = 0, nums[-1]
    while i <= j:
        m = (i + j) >> 1
        if nums[m] == m:
            i = m + 1
        else:
            j = m - 1
    return i

if __name__ == "__main__" :
    nums = [0,1,2,3,4,5,6,7,9]
    result = missingNumber(nums)
    print(result)