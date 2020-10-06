class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSubStructure(A: TreeNode, B: TreeNode) -> bool:
    def dfs(A,B) -> bool :
        if not B :
            return True
        if not A or A.val != B.val :
            return False
        return dfs(A.left,B.left) and dfs(A.right,B.right)
    if not A or not B :
        return False
    return dfs(A,B) or isSubStructure(A.left,B) or isSubStructure(A.right, B)


if __name__ == "__main__" :
    node = TreeNode(3)
    node.left = TreeNode(5)
    node.right = TreeNode(1)
    node.left.left = TreeNode(6)
    node.left.right = TreeNode(2)
    node.right.left = TreeNode(7)

    node1 = TreeNode(1)
    node1.left = TreeNode(7)
    result = isSubStructure(node,node1)
    print(result)

