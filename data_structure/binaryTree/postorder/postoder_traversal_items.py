
# 二叉树的中序遍历

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 迭代
def postorderTraversal(root: TreeNode) ->[int]:
    result = []
    queue = [root]
    while queue:
        root = queue.pop()
        if root:
            result.append(root.val)
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
    return result[::-1]


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)

    root.right.left = TreeNode(3)
    result = postorderTraversal(root)
    print(result)
