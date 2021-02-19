def exist(board: [[str]], word: str) -> bool:
    m = len(board)
    if m == 0 :
        return False
    n = len(board[0])
    def dfs(i,j,k) :
        if (i < 0 or i >= m) or (j < 0 or j >= n) or (board[i][j] != word[k]) :
            return False
        if k == len(word) - 1 :
            return True
        tmp , board[i][j] = board[i][j], '/'
        res = dfs(i+1,j,k+1) or dfs(i,j+1,k+1) or dfs(i-1,j,k+1) or dfs(i,j-1,k+1)
        board[i][j] = tmp
        return res
    for i in range(m) :
        for j in range(n) :
            if dfs(i,j,0) :
                return True
    return False

if __name__ == "__main__" :
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    result = exist(board,word)
    print(result)