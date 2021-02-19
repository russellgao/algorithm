def uniquePathsWithObstacles(obstacleGrid: [[int]]) -> int:
    m,n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [0] * n
    if obstacleGrid[0][0] == 0 :
        dp[0] = 1
    for i in range(m) :
        for j in range(n) :
            if obstacleGrid[i][j] == 1 :
                dp[j] = 0
                continue
            if j >= 1 and obstacleGrid[i][j-1] == 0 :
                dp[j] += dp[j-1]
    return dp[n-1]

if __name__ == "__main__" :
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    result = uniquePathsWithObstacles(obstacleGrid)
    print(result)

