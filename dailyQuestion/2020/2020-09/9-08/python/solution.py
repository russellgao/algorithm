import copy
def combinationSum(candidates: [int], target: int) -> [[int]]:
    result = []
    temp = []

    def dfs(target, idx):
        if idx == len(candidates):
            return
        if target == 0:
            comb = copy.deepcopy(temp)
            result.append(comb)
            return
        dfs(target, idx + 1)
        if target - candidates[idx] >= 0:
            temp.append(candidates[idx])
            dfs(target - candidates[idx], idx)
            temp.pop()

    dfs(target, 0)
    return result


if __name__ == "__main__" :
    result = combinationSum([2,3,6,7],7)
    print(result)
