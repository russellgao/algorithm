def generateParenthesis(n: int) -> [str]:
    result = []
    def dfs(S, left, right) :
        if len(S) == 2 * n :
            result.append("".join(S))
            return
        if left < n :
            S.append("(")
            dfs(S, left+1 , right)
            S.pop()
        if right < left :
            S.append(")")
            dfs(S,left,right+1)
            S.pop()
    dfs([],0,0)
    return result

if __name__ == "__main__" :
    n = 3
    result = generateParenthesis(n)
    print(result)
