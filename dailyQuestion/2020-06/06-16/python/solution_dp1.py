def minPathSum(grid: [[int]]) -> int:
    if not grid :
        return 0
    m = len(grid)
    n = len(grid[0])
    for i in range(m) :
        for j in range(n) :
            if j == 0 and i == 0 :
                continue
            if j == 0 :
                grid[i][j] = grid[i-1][j] + grid[i][j]
            elif i == 0 :
                grid[i][j] = grid[i][j-1] + grid[i][j]
            else :
                grid[i][j] = grid[i][j] + min(grid[i][j-1],grid[i-1][j])
    return grid[m-1][n-1]

if __name__ == "__main__" :
    grid = [[1,3,1],
            [1,5,1],
            [4,2,1]]
    result = minPathSum(grid)
    print(result)