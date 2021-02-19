def findRepeatNumber(nums: [int]) -> int:
    tmp = {}
    for num in nums :
        if num in tmp :
            return num
        else :
            tmp[num] = True
    return

if __name__ == "__main__" :
    nums = [2, 3, 1, 0, 2, 5, 3]
    result = findRepeatNumber(nums)
    print(result)
