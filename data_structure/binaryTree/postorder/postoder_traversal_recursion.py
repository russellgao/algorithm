
# 二叉树的前序遍历

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归
def postorderTraversal(root: TreeNode) -> [int]:
    result = []
    if not root:
        return result
    left = postorderTraversal(root.left)
    result.extend(left)
    right = postorderTraversal(root.right)
    result.extend(right)
    result.append(root.val)
    return result



if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)

    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)

    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    result = postorderTraversal(root)
    print(result)