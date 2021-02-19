# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def hasPathSum(root: TreeNode, sum: int) -> bool:
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == sum
    return hasPathSum(root.left, sum - root.val) or hasPathSum(root.right, sum - root.val)

if __name__ == "__main__" :
    node = TreeNode(5)
    node.left = TreeNode(4)
    node.left.left = TreeNode(11)
    node.left.left.left = TreeNode(7)
    node.left.left.right = TreeNode(2)
    node.right = TreeNode(8)
    node.right.right = TreeNode(4)
    node.right.right.right = TreeNode(1)
    result = hasPathSum(node,22)
    print(result)
