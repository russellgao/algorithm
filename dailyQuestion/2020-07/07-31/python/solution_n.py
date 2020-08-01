def missingTwo(nums: [int]) -> [int]:
    ret = 0
    for i, num in enumerate(nums):
        ret ^= (i + 1)
        ret ^= num
    ret ^= len(nums) + 1
    ret ^= len(nums) + 2
    mask = 1
    while mask & ret == 0:
        mask <<= 1
    a, b = 0, 0
    for i in range(1, len(nums) + 3):
        if i & mask:
            a ^= i
        else:
            b ^= i
    for num in nums:
        if num & mask:
            a ^= num
        else:
            b ^= num
    return [a, b]

if __name__ == "__main__" :
    nums = [2,3]
    result = missingTwo(nums)
    print(result)
