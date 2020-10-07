def sortColors(nums: [int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    p0, p2 = 0, n-1
    i = 0
    while i <= p2 :
        while i <= p2 and nums[i] == 2 :
            nums[i] , nums[p2] = nums[p2],nums[i]
            p2 -=1
        if nums[i] == 0 :
            nums[i] , nums[p0] = nums[p0] , nums[i]
            p0 += 1
        i += 1


if __name__ == "__main__" :
    nums = [2,0,2,1,1,0]
    sortColors(nums)
    print(nums)