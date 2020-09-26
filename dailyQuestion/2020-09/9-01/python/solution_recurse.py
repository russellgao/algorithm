# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def pathSum(root: TreeNode, sum: int) -> [[int]]:
    temp = []
    result = []
    def dfs(root: TreeNode, left: int) :
        if not root :
            return
        left -= root.val
        temp.append(root.val)
        if not root.left and not root.right and left == 0 :
            result.append(temp[:])
        dfs(root.left,left)
        dfs(root.right,left)
        temp.pop()

    dfs(root,sum)
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
    result = pathSum(node,12)
    print(result)
