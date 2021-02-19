def productExceptSelf( nums: [int]) -> [int]:
    n = len(nums)
    left, right , result = [0] * n , [0] * n , [0] * n
    left[0] = 1
    right[n-1] = 1
    for i in range(1,n) :
        left[i] = left[i-1] * nums[i-1]
    for i in range(n-2,-1,-1) :
        right[i] = right[i+1] * nums[i+1]
    for i in range(n) :
        result[i] = left[i] * right[i]
    return result

if __name__ == "__main__" :
    nums = [1,2,3,4]
    result = productExceptSelf(nums)
    print(result)

