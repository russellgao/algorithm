from functools import reduce


# 位运算 写法1
def singleNumber1(nums: [int]) -> int:
    return reduce(lambda x, y: x ^ y, nums)

# 位运算 写法2
def singleNumber2(nums: [int]) -> int :
    result = nums[0]
    for i in range(1,len(nums)) :
        result ^= nums[i]
    return result

if __name__ == "__main__" :
    nums = [2,3,4,3,2]
    print(singleNumber2(nums))