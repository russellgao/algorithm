def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_num = nums[0]
    for i in range(1,len(nums)) :
        if nums[i] + nums[i-1] > nums[i] :
            nums[i] = nums[i] + nums[i-1]
        if nums[i] > max_num :
            max_num = nums[i]
    return max_num

if __name__ == "__main__" :
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    max_num = maxSubArray(nums)
    print(max_num)