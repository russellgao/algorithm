class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def countNodes(root: TreeNode) -> int:

    def compute_path(root):
        d = 0
        while root.left:
            d += 1
            root = root.left
        return d

    def exists(idx, d, node):
        left, right = 0, 2 ** d - 1
        for _ in range(d):
            mid = left + (right - left) // 2
            if idx <= mid:
                node = node.left
                right = mid
            else:
                node = node.right
                left = mid + 1
        return node is not None

    if not root:
        return 0
    d = compute_path(root)
    if d == 0:
        return 1
    left, right = 1, 2 ** d - 1
    while left <= right:
        mid = left + (right - left) // 2
        if exists(mid, d, root):
            left = mid + 1
        else:
            right = mid - 1
    return (2 ** d - 1) + left

if __name__ == "__main__" :
    node = TreeNode(3)
    node.left = TreeNode(5)
    node.right = TreeNode(1)
    node.left.left = TreeNode(6)
    node.left.right = TreeNode(2)
    node.right.left= TreeNode(7)

    result = countNodes(node)
    print(result)