def permute(nums: [int]) -> [[int]]:
    result = []
    n = len(nums)
    def dfs(cur) :
        if cur == n :
            result.append(nums[:])
            return
        for i in range(cur,n) :
            nums[i],nums[cur] = nums[cur],nums[i]
            dfs(cur+1)
            nums[i],nums[cur] = nums[cur],nums[i]
    dfs(0)
    return result

if __name__ == "__main__" :
    result = permute([1,2,3])
    print(result)
