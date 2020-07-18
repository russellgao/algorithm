def isInterleave(s1, s2, s3):
    """
    :type s1: str
    :type s2: str
    :type s3: str
    :rtype: bool
    """
    m = len(s1)
    n = len(s2)
    t = len(s3)
    if m + n != t:
        return False
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    for i in range(m + 1):
        for j in range(n + 1):
            if i > 0:
                dp[i][j] = dp[i][j] or (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1])
            if j > 0:
                dp[i][j] = dp[i][j] or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
    return dp[m][n]

if __name__ == "__main__" :
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    result = isInterleave(s1,s2,s3)
    print(result)

