def longestValidParentheses(s: str) -> int:
    result = 0
    if not s:
        return result
    n = len(s)
    stack = [-1]
    for i in range(n):
        if s[i] == "(":
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                result = max(result, i - stack[len(stack) - 1])
    return result

if __name__ == "__main__" :
    s = "(())()"
    result = longestValidParentheses(s)
    print(result)
