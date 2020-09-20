def subsets(nums: [int]) -> [[int]]:
    result = []
    temp = []
    n = len(nums)
    def dfs(idx) :
        if idx == n :
            result.append(temp[:])
            return
        temp.append(nums[idx])
        dfs(idx +1)
        temp.pop()
        dfs(idx+1)
    dfs(0)
    return result


if __name__ == "__main__" :
    result = subsets([1,2,3])
    print(result)