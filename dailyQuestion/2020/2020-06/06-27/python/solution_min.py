def firstMissingPositive(nums: [int]) -> int:
    min_num = float('inf')
    for item in nums:
        if item <= 0:
            continue
        min_num = min(min_num, item)

    if min_num != 1 or min_num < 0:
        return 1
    else:
        while min_num in nums:
            min_num += 1
    return min_num

if __name__ == "__main__" :
    nums = [1,2,3,0]
    result = firstMissingPositive(nums)
    print(result)
