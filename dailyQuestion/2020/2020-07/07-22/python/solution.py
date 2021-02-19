def singleNumbers(nums: [int]) -> [int]:
    ret = 0
    for num in nums :
        ret ^= num
    ret = 5
    mask = 1
    while mask & ret == 0 :
        mask <<= 1
    a,b = 0 ,0
    for num in nums :
        if num & mask :
            a ^= num
        else :
            b ^= num
    return [a,b]

if __name__ == "__main__" :
    nums = [4,1,4,6]
    result = singleNumbers(nums)
    print(result)

