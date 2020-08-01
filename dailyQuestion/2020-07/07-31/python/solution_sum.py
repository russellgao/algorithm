def missingTwo(nums: [int]) -> [int]:
    n = len(nums) + 2
    sum_nums = 0
    for num in nums:
        sum_nums += num
    sumTwo = int((n * (n + 1) / 2) - sum_nums)
    limit = sumTwo >> 1
    sum_nums = 0
    for num in nums:
        if num <= limit:
            sum_nums += num
    one = int(limit * (limit + 1) / 2 - sum_nums)
    return [one, sumTwo - one]

if __name__ == "__main__" :
    nums = [2,3]
    result = missingTwo(nums)
    print(result)
