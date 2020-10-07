def removeDuplicates(nums: [int]) -> int:
    i , count = 1,1
    for j in range(1,len(nums)) :
        if nums[j] == nums[j-1] :
            count += 1
        else :
            count =1
        if count <= 2 :
            nums[i] = nums[j]
            i += 1
    return i


if __name__ == "__main__" :
    reslu = removeDuplicates([1,1,1,1,1,2,2,2,2,2,3,4,5,6,7])
    print(reslu)
