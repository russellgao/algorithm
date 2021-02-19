def findLength(A: [int], B: [int]) -> int:
    n, m = len(A), len(B)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    ans = 0
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            dp[i][j] = dp[i + 1][j + 1] + 1 if A[i] == B[j] else 0
            ans = max(ans, dp[i][j])
    return ans


if __name__ == "__main__" :

    A = [1,2,3,2,1]
    B = [3,2,1,4,7]

    a = A[0:1] == B[2:3]
    result = findLength(A,B)
    print(result)
