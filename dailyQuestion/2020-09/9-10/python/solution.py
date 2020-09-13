import copy
def combinationSum3(k: int, n: int) -> [[int]]:
    result = []
    temp = []
    def dfs(target, idx) :
        if target == 0 and len(temp) == k :
            comb = copy.deepcopy(temp)
            result.append(comb)
            return
        if target <= 0 or len(temp) >= k :
            return
        if idx < 10 :
            dfs(target, idx+1)
            temp.append(idx)
            dfs(target - idx , idx+1)
            temp.pop()
    dfs(n,1)
    return result

if __name__ == "__main__" :
    result = combinationSum3(3,8)
    print(result)