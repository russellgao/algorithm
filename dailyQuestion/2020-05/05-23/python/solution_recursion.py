# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(preorder: [int], inorder: [int]) -> TreeNode:
    def tmp_build_tree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int) -> TreeNode:
        if preorder_left > preorder_right:
            return None
        # 前序遍历的root 节点
        preorder_root = preorder_left
        # 中序遍历的root 节点
        inorder_root = index[preorder[preorder_root]]

        # 构造根节点
        root = TreeNode(preorder[preorder_root])

        # 中序遍历左子树的长度
        inorder_left_size = inorder_root - inorder_left
        # 构造左子树
        root.left = tmp_build_tree(preorder_left + 1, preorder_left + inorder_left_size, inorder_left,
                                   inorder_root - 1)
        # 构造右子树
        root.right = tmp_build_tree(preorder_left + inorder_left_size + 1, preorder_right, inorder_root + 1,
                                    inorder_right)
        return root

    n = len(inorder)
    index = {key: i for i, key in enumerate(inorder)}
    return tmp_build_tree(0, n - 1, 0, n - 1)


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    node = buildTree(preorder, inorder)
    print()
