class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0
    height = 0
    queue = [root]
    while queue:
        size = len(queue)
        height += 1
        stack = []
        while size != 0:
            node = queue.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            size -= 1
        queue.extend(stack)
    return height



if __name__ == "__main__" :
    node = TreeNode(3)
    node.left = TreeNode(9)
    node.left.left = TreeNode(5)
    node.left.right = TreeNode(8)
    node.right = TreeNode(20)
    node.right.left = TreeNode(15)
    node.right.right = TreeNode(7)
    result = maxDepth(node)
    print(result)

