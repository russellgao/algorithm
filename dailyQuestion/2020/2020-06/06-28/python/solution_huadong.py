def minSubArrayLen(s: int, nums: [int]) -> int:
    if not nums :
        return 0
    n = len(nums)
    result = float('inf')
    start = end = sum_n = 0
    while end < n :
        sum_n += nums[end]
        while sum_n >= s :
            result = min(result,end-start+1)
            sum_n -= nums[start]
            start += 1
        end += 1
    if result == float('inf') :
        return 0
    return result

if __name__ == "__main__" :
    s = 7
    nums = [2,3,1,2,4,3]
    result = minSubArrayLen(s,nums)
    print(result)

