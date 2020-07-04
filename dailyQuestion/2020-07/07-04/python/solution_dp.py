def longestValidParentheses(s: str) -> int:
    result = 0
    if not s:
        return result
    n = len(s)
    dp = [0] * n
    for i in range(1, n):
        if s[i] == ")":
            if s[i - 1] == "(":
                dp[i] = dp[i - 2] + 2
            elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == "(":
                if i - dp[i - i] >= 2:
                    dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                else:
                    dp[i] = dp[i - 1] + 2
            result = max(result, dp[i])
    return result


if __name__ == "__main__":
    s = "((()))()"
    result = longestValidParentheses(s)
    print(result)
