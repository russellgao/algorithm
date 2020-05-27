

# 位运算求解
def findDuplicate(nums: [int]) -> int :
    n = len(nums)
    bit_max = 32
    result = 0
    while (n-1) >> bit_max == 0 :
        bit_max -= 1
    for bit in range(bit_max) :
        x, y = 0 ,0
        for i in range(n) :
            if nums[i] & 1 << bit > 0 :
                x += 1
            if i > 0 and i & 1 << bit > 0 :
                y += 1
        if x > y :
            result |= 1 << bit
    return result


if __name__ == "__main__" :
    nums = [1,3,4,2,1]
    result = findDuplicate(nums)
    print(result)

