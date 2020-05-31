# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 迭代
def isSymmetric(root: TreeNode) -> bool:
    queue = [root, root]
    while queue:
        left, right = queue[:2]
        queue = queue[2:]
        if not left and not right:
            continue
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        queue.extend([left.left, right.right, left.right, right.left])
    return True


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)

    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)

    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    result = isSymmetric(root)
    print(result)
