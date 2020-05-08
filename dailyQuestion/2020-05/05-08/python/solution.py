
# 动态规划
# 以右下角为正方形开始计算
def maximalSquare(matrix) -> int:
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0
    maxSide = 0
    rows, columns = len(matrix), len(matrix[0])
    dp = [[0] * columns for i in range(rows)]
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == '1':
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                maxSide = max(maxSide, dp[i][j])
    return maxSide * maxSide

# 时间复杂度: o(m*n)
# 空间复杂度: o(m*n) , 因为新开辟出来相同大小的空间

if __name__ == "__main__" :
    matrix = [["1"]]
    result = maximalSquare(matrix)
    print(result)
