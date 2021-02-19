# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def pathSum(root: TreeNode, sum: int) -> [[int]]:
    result = []
    if not root :
        return result
    def getpath(node) :
        temp = []
        while node :
            temp.append(node.val)
            node = parent.get(node)
        result.append(temp[::-1])

    parent = {}
    stack = [{"node":root, "left":sum}]
    while stack :
        p = stack[0]
        stack = stack[1:]
        node = p["node"]
        left = p["left"]
        left -= node.val
        if not node.left and not node.right :
            if left == 0 :
                getpath(node)
        else :
            if node.left :
                parent[node.left] = node
                stack.append({"node":node.left,"left":left})
            if node.right :
                parent[node.right] = node
                stack.append({"node":node.right,"left":left})
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