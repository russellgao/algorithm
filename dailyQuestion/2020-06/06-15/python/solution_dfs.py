class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def rserialize(root, s):
            if not root:
                s += "null,"
                return s
            s += "{},".format(root.val)
            s = rserialize(root.left, s)
            s = rserialize(root.right, s)
            return s

        return rserialize(root, "")

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        l = []
        _tmp = data.split(",")
        for item in _tmp:
            if item:
                l.append(item)
        l.reverse()

        def rdeserialize():
            if not l:
                return None
            val = l.pop()
            if val == "null":
                return None
            root = TreeNode(val)
            root.left = rdeserialize()
            root.right = rdeserialize()
            return root

        return rdeserialize()

if __name__ == "__main__" :
    codec = Codec()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    data = codec.serialize(root)
    result = codec.deserialize(data)
    print(result)
