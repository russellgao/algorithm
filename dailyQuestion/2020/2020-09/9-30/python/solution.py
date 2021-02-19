class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def listOfDepth(tree: TreeNode) -> [ListNode]:
    result = []
    if not tree :
        return result
    queue = [tree]
    while len(queue) > 0 :
        size = len(queue)
        listnode = ListNode(0)
        tmp = listnode
        while size > 0 :
            node = queue[0]
            queue = queue[1:]
            tmp.next = ListNode(node.val)
            tmp = tmp.next
            if node.left :
                queue.append(node.left)
            if node.right :
                queue.append(node.right)
            size -= 1
        result.append(listnode.next)
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

    result = listOfDepth(node)
    print(result)