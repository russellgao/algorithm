class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sumOfLeftLeaves(root: TreeNode) -> int:
    result = 0
    if not root :
        return result
    if root.left and not root.left.left and not root.left.right :
        result += root.left.val
    result += sumOfLeftLeaves(root.left)
    result += sumOfLeftLeaves(root.right)
    return result

if __name__ == "__main__" :
    node = TreeNode(3)
    node.left = TreeNode(5)
    node.right = TreeNode(1)
    node.left.left = TreeNode(6)
    node.left.right = TreeNode(2)
    node.left.right.left = TreeNode(7)
    node.left.right.right = TreeNode(4)

    node.right.left = TreeNode(0)
    node.right.right = TreeNode(8)
    result = sumOfLeftLeaves(node)
    print(result)

