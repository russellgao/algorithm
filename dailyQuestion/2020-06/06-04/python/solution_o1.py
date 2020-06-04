def productExceptSelf(nums: [int]) -> [int]:
    n = len(nums)
    result = [0] * n
    result[0] = 1
    for i in range(1,n) :
        result[i] = result[i-1] * nums[i-1]
    tmp = 1
    for i in range(n-2,-1,-1) :
        tmp *= nums[i+1]
        result[i] = result[i] * tmp
    return result

if __name__ == "__main__" :
    nums = [1,2,3,4]
    result = productExceptSelf(nums)
    print(result)


