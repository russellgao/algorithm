
# 二叉树的中序遍历

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 迭代
def preorderTraversal(root: TreeNode) ->[int]:
    result = []
    if not root:
        return result
    queue = [root]
    while queue:
        root = queue.pop()
        if root:
            result.append(root.val)
            if root.right:
                queue.append(root.right)
            if root.left:
                queue.append(root.left)
    return result


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)

    root.right.left = TreeNode(3)
    result = preorderTraversal(root)
    print(result)
