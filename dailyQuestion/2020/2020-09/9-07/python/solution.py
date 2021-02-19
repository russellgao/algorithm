import copy
def combine(n: int, k: int) -> [[int]]:
    result = []
    temp = []
    def dfs(cur: int) :
        if len(temp) + (n-cur+1) < k :
            return
        if len(temp) == k :
            comb = copy.deepcopy(temp)
            result.append(comb)
            return
        temp.append(cur)
        dfs(cur+1)
        temp.pop()
        dfs(cur+1)
    dfs(1)
    return result

if __name__ == "__main__" :
    result = combine(4,2)
    print(result)