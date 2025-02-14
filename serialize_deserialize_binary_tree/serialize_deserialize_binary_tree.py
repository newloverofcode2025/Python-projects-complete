class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string."""
        def dfs(node):
            if not node:
                return "null,"
            return str(node.val) + "," + dfs(node.left) + dfs(node.right)
        return dfs(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        def dfs(nodes):
            val = next(nodes)
            if val == "null":
                return None
            node = TreeNode(int(val))
            node.left = dfs(nodes)
            node.right = dfs(nodes)
            return node
        return dfs(iter(data.split(',')))

# Helper function to print the tree in pre-order traversal
def print_tree_preorder(root):
    if not root:
        return "null"
    return str(root.val) + " " + print_tree_preorder(root.left) + " " + print_tree_preorder(root.right)

if __name__ == "__main__":
    # Create a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    codec = Codec()
    serialized = codec.serialize(root)
    print(f"Serialized Tree: {serialized}")

    deserialized = codec.deserialize(serialized)
    print(f"Deserialized Tree Pre-order: {print_tree_preorder(deserialized)}")