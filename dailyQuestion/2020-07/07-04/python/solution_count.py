def longestValidParentheses(s: str) -> int:
    result = 0
    if not s:
        return result
    n = len(s)
    left, right = 0, 0
    for i in range(n):
        if s[i] == "(":
            left += 1
        else:
            right += 1
        if left == right:
            result = max(result, left + right)
        elif left < right:
            left, right = 0, 0
    left, right = 0, 0
    for i in range(n - 1, -1, -1):
        if s[i] == "(":
            left += 1
        else:
            right += 1
        if left == right:
            result = max(result, left + right)
        if left > right:
            left, right = 0, 0
    return result


if __name__ == "__main__":
    s = "(())()"
    result = longestValidParentheses(s)
    print(result)
