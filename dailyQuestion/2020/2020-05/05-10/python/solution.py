class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 方法一
# 递归
def lowestCommonAncestor1( root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root:
        return None
    if root.val == p.val or root.val == q.val:
        return root
    left = lowestCommonAncestor1(root.left, p, q)
    right = lowestCommonAncestor1(root.right, p, q)
    if left and right:
        return root
    if not left:
        return right
    return left

# 方法二
# 存储父节点
def lowestCommonAncestor2(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    parent = {}
    vistor = {}

    def dfs(root):
        if not root:
            return
        if root.left:
            parent[root.left.val] = root
            dfs(root.left)
        if root.right:
            parent[root.right.val] = root
            dfs(root.right)

    dfs(root)
    while p:
        vistor[p.val] = True
        p = parent.get(p.val)
    while q:
        if vistor.get(q.val):
            return q
        q = parent.get(q.val)
    return

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

    p = TreeNode(5)
    q = TreeNode(1)
    result = lowestCommonAncestor2(node,p,q)
    print(result.val)