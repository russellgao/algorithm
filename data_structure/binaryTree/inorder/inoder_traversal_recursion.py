
# 二叉树的中序遍历

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 迭代
def inorderTraversal(root: TreeNode) ->[int]:
    result = []
    queue = []
    while root or queue :
        while root :
            queue.append(root)
            root = root.left
        node = queue.pop()
        result.append(node.val)
        root = node.right
    return result



if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)

    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)

    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    result = inorderTraversal(root)
    print(result)