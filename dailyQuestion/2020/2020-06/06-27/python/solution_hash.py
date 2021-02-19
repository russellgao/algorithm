def firstMissingPositive(nums: [int]) -> int:
    n = len(nums)
    for i in range(n):
        if nums[i] <= 0:
            nums[i] = n + 1
    for i in range(n):
        num = abs(nums[i])
        if num <= n:
            nums[num - 1] = -abs(nums[num - 1])
    for i in range(n):
        if nums[i] > 0:
            return i + 1
    return n + 1

if __name__ == "__main__" :
    nums = [1,2,3,0]
    result = firstMissingPositive(nums)
    print(result)
