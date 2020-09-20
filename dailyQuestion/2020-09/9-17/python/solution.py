def permuteUnique(nums: [int]) -> [[int]]:
    result = []
    temp = []
    nums.sort()
    n = len(nums)
    visitd = [False for i in range(n)]
    def dfs(idx: int) :
        if idx == n :
            result.append(temp[:])
            return
        for i in range(n) :
            if visitd[i] or (i > 0 and nums[i] == nums[i-1] and not visitd[i-1]) :
                continue
            temp.append(nums[i])
            visitd[i] = True
            dfs(idx+1)
            temp.pop()
            visitd[i] = False
    dfs(0)
    return result

if __name__ == "__main__" :
    permuteUnique([2,1,1])