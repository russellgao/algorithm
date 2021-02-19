def countNumbersWithUniqueDigits(n: int) -> int:
    if n == 0 :
        return 1
    used = [False] * 10
    def dfs(idx: int) -> int:
        if idx == n :
            return 0
        result = 0
        for num in range(10) :
            if n >= 2 and idx == 1 and num == 0 :
                continue
            if used[num] :
                continue
            used[num] = True
            result += dfs(idx + 1) + 1
            used[num] = False
        return result
    return dfs(0)

if __name__ == "__main__" :
    result = countNumbersWithUniqueDigits(2)
    print(result)