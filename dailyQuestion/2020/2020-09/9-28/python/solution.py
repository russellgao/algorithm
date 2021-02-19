# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    result = root
    while True :
        if p.val < result.val and q.val < result.val :
            result = result.left
        elif p.val > result.val and q.val > result.val :
            result = result.right
        else :
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

    p = TreeNode(5)
    q = TreeNode(1)
    result = lowestCommonAncestor(node,p,q)
    print(result.val)