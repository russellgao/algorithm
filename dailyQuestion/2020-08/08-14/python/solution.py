def isValid(s: str) -> bool:
    if not s:
        return True
    tmp = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for item in s:
        if not stack and item in [")", "]", "}"]:
            return False
        if item in tmp:
            stack.append(item)
            continue
        tmp_item = stack.pop()
        if item != tmp[tmp_item]:
            return False
    if len(stack) > 0:
        return False
    return True


if __name__ == "__main__" :
    s = "([)]"
    print(isValid(s))
