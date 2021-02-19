# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self) :
        self.maxPath = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        def recurse(root) :
            if not root :
                return 0
            leftMax = max(recurse(root.left),0)
            rightMax = max(recurse(root.right),0)
            self.maxPath = max(self.maxPath, root.val + leftMax + rightMax)
            return root.val + max(leftMax , rightMax)
        recurse(root)
        return int(self.maxPath)

if __name__ == "__main__" :
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    s = Solution()
    result = s.maxPathSum(root)
    print(result)
