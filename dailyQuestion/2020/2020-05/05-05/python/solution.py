class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 方法一
# 中序遍历，中序遍历是一个升序的队列
def isValidBST(root: TreeNode) -> bool:
    """

    :param root:
    :return:
    """
    stack, inorder = [], float('-inf')
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if root.val <= inorder:
            return False
        inorder = root.val
        root = root.right
    return True

# 方法二
# 递归
def isValidBST_2(root: TreeNode) -> bool:
    """

    :param root:
    :return:
    """
    return helper(root, float('-inf'), float('+inf'))


def helper(root: TreeNode, lower: float, upper: float) -> bool:
    if not root:
        return True
    if root.val <= lower or root.val >= upper:
        return False
    return helper(root.left, lower, root.val) and helper(root.right, root.val, upper)


if __name__ == "__main__":
    node = TreeNode(5)
    node.left = TreeNode(1)
    node.right = TreeNode(7)

    node.right.left = TreeNode(6)
    node.right.right = TreeNode(8)

    result = isValidBST_2(node)
    print()
