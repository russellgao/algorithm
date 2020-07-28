class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxDepth(root: TreeNode) -> int:
    if not root :
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1

if __name__ == "__main__" :
    node = TreeNode(3)
    node.left = TreeNode(9)
    node.right = TreeNode(20)
    node.right.left = TreeNode(15)
    node.right.right = TreeNode(7)
    result = maxDepth(node)
    print(result)

