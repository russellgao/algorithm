# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def increasingBST(root: TreeNode) -> TreeNode:
    result = node = TreeNode(0)
    queue = []
    while root or len(queue) > 0 :
        while root :
            queue.append(root)
            root = root.left
        root = queue[len(queue)-1]
        queue = queue[:len(queue)-1]
        node.right = TreeNode(root.val)
        node = node.right
        root = root.right
    return result.right

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

    result = increasingBST(node)
    print(result)