def subsetsWithDup(nums: [int]) -> [[int]]:
    result = []
    nums.sort()
    def dfs(temp: [int] , idx: int) :
        result.append(temp[:])
        for i in range(idx,len(nums)) :
            if i > idx and nums[i] == nums[i-1] :
                continue
            temp.append(nums[i])
            dfs(temp,i+1)
            temp.pop()
    dfs([],0)
    return result


if __name__ == "__main__" :
    result = subsetsWithDup([1,2,2])
    print(result)
