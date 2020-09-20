def removeElement(nums: [int], val: int) -> int:
    i , n = 0 , len(nums)
    while i < n :
        if nums[i] == val :
            nums[i] = nums[n-1]
            n -= 1
        else :
            i += 1
    return n

if __name__ == "__main__" :
    result = removeElement([3,2,3,2], 3)
    print(result)