def sortColors(nums: [int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    ptr = 0
    for i in range(n) :
        if nums[i] == 0 :
            nums[i] , nums[ptr] = nums[ptr] , nums[i]
            ptr += 1
    for i in range(n) :
        if nums[i] == 1 :
            nums[i], nums[ptr] = nums[ptr] , nums[i]
            ptr += 1

if __name__ == "__main__" :
    nums = [2,0,2,1,1,0]
    sortColors(nums)
    print(nums)

