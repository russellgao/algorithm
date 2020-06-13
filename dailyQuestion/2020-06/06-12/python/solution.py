def threeSum(nums: [int]) -> [[int]]:
    nums.sort()
    result = []
    n = len(nums)
    if not nums or nums[0] > 0 or nums[-1] < 0 :
        return result
    for first in range(n) :
        if first > 0 and nums[first] == nums[first-1] :
            continue
        third = n-1
        target = -nums[first]
        for second in range(first+1,n) :
            if second > first + 1 and nums[second] == nums[second-1] :
                continue
            while second < third and nums[second] + nums[third] > target:
                third -= 1
            if second == third :
                break
            if nums[second] + nums[third] == target:
                result.append([nums[first],nums[second],nums[third]])
    return result


if __name__ == "__main__" :
    nums = [-1,0,1,2,-1,-4]
    result = threeSum(nums)
    print(result)
