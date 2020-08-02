
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten(root: TreeNode) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    if not root :
        return
    cur = root
    while cur :
        if cur.left :
            next = cur.left
            pre = next
            while pre.right :
                pre = pre.right
            pre.right = cur.right
            cur.left = None
            cur.right = next
        cur = cur.right

if __name__ == "__main__" :
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)
    flatten(root)
