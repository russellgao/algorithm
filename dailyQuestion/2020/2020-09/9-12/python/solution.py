class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def averageOfLevels(root: TreeNode) -> [float]:
    result = []
    stack = [root]
    while stack :
        sum_s = 0
        size = len(stack)
        for i in range(size) :
            node = stack[0]
            stack = stack[1:]
            sum_s += node.val
            if node.left :
                stack.append(node.left)
            if node.right :
                stack.append(node.right)
        result.append(sum_s / size)
    return result

if __name__ == "__main__" :
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(17)
    root.right.right = TreeNode(7)
    result = averageOfLevels(root)
    print(result)

