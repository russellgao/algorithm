# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归
def isSymmetric(root: TreeNode) -> bool:
    def check(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right and check(left.left, right.right) and check(left.right, right.left)

    return check(root, root)


if __name__ == "__main__":
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(2)
    #
    # root.left.left = TreeNode(3)
    # root.left.right = TreeNode(4)
    #
    # root.right.left = TreeNode(4)
    # root.right.right = TreeNode(3)

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)

    root.left.left = TreeNode(3)
    root.right.right = TreeNode(3)
    result = isSymmetric(root)
    print(result)
