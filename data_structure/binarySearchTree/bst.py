# 节点定义
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 查找
def search(root: TreeNode, val: int) -> (bool, TreeNode):
    if root == None:
        return False, None
    elif val > root.val:
        return search(root.right, val)
    elif val < root.val:
        return search(root.left, val)
    else:
        return True, root


# 插入
def insert(root: TreeNode, node: TreeNode) -> TreeNode:
    """insert inplace"""
    if root == None:
        root = node
        return root
    elif node.val > root.val:
        root.right = insert(root.right, node)
    else:
        root.left = insert(root.left, node)
    return root


# 删除
def deleteNode(root: TreeNode, key: int) -> TreeNode:
    """
    :type root: TreeNode
    :type key: int
    :rtype: TreeNode
    """
    if root == None:
        return None
    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        if root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        else:
            min_node = findMinNode(root.right)
            root.val = min_node.val
            root.right = deleteNode(root.right, root.val)
    return root


def findMinNode(node: TreeNode) -> TreeNode:
    while node.left:
        node = node.left
    return node


# 中序遍历
def traverse_binary_tree(root: TreeNode):
    if root is None:
        return
    traverse_binary_tree(root.left)
    print(root.val)
    traverse_binary_tree(root.right)


# 构建二叉树
def build_binary_tree(values: [int]):
    tree = None
    for v in values:
        tree = insert(tree, TreeNode(v))
    return tree


if __name__ == "__main__":
    values = [17, 5, 35, 2, 11, 29, 38, 9, 16, 7]
    # 构造二叉树
    node = build_binary_tree(values)

    # 查找
    node_7 = search(node, 35)

    # 遍历
    traverse_binary_tree(node)

    # 删除
    a = deleteNode(node, 5)

    print()
