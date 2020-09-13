import copy
def partition(s: str) -> [[str]]:
    result = []
    temp = []
    n = len(s)

    def check(i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def dfs(start):
        if start == n:
            comb = copy.deepcopy(temp)
            result.append(comb)
            return
        for i in range(start, n):
            if not check(start, i):
                continue
            temp.append(s[start:i+1])
            dfs(i + 1)
            temp.pop()

    dfs(0)
    return result

if __name__ == "__main__" :
    result = partition("aab")
    print(result)