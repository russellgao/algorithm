class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 方法一
# 递归
def lowestCommonAncestor( root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root:
        return None
    if root.val == p.val or root.val == q.val:
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if left and right:
        return root
    if not left:
        return right
    return left



if __name__ == "__main__" :
    node = TreeNode(3)
    node.left = TreeNode(5)
    node.right = TreeNode(1)
    node.left.left = TreeNode(6)
    node.left.right = TreeNode(2)
    node.left.right.left = TreeNode(7)
    node.left.right.right = TreeNode(2)

    node.right.left = TreeNode(0)
    node.right.right = TreeNode(8)

    p = TreeNode(5)
    q = TreeNode(1)
    result = lowestCommonAncestor(node,p,q)
    print(result.val)