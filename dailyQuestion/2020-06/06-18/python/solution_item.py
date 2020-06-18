class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def recoverFromPreorder(S: str) -> TreeNode:
    if not S:
        return None
    stack, pos = list(), 0
    while pos < len(S):
        level = 0
        while S[pos] == "-":
            pos += 1
            level += 1
        value = 0
        while pos < len(S) and S[pos].isdigit():
            value = value * 10 + int(S[pos])
            pos += 1
        node = TreeNode(value)
        if level == len(stack):
            if stack:
                stack[-1].left = node
        else:
            stack = stack[:level]
            stack[-1].right = node
        stack.append(node)
    return stack[0]


if __name__ == "__main__":
    S = "1-2--3--4-5--6--7"
    result = recoverFromPreorder(S)
    print(result)
