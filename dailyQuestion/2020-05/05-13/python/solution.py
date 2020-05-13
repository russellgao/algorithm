class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def levelOrder(root: TreeNode) -> [[int]]:
    result = []
    if not root:
        return result
    q = [root]
    i = 0
    while len(q) > 0:
        p = []
        result.append([])
        for j in range(len(q)):
            node = q[j]
            result[i].append(node.val)
            if node.left:
                p.append(node.left)
            if node.right:
                p.append(node.right)
        i += 1
        q = p
    return result


if __name__ == "__main__":
    node = TreeNode(3)
    node.left = TreeNode(5)
    node.right = TreeNode(1)
    node.left.left = TreeNode(6)
    node.left.right = TreeNode(2)
    node.left.right.left = TreeNode(7)
    node.left.right.right = TreeNode(4)

    node.right.left = TreeNode(0)
    node.right.right = TreeNode(8)

    p = TreeNode(5)
    q = TreeNode(1)
    result = levelOrder(node)
    print(result)
