# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sortedArrayToBST(nums: [int]) -> TreeNode:
    n = len(nums)
    if not nums :
        return None
    mid = n >> 1
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])
    return root

if __name__ == "__main__" :
    nums = [-10,-3,0,5,9]
    result = sortedArrayToBST(nums)
    print(result)
