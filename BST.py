# %%
class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'
    
class BinarySearchTree:
    def __init__(self, tree_data):
        self.root = None
        if tree_data:
            self.root = TreeNode(tree_data[0])
            for value in tree_data[1:]:
                self.insert(self.root, value)

    def insert(self, node, value):
        if value <= node.data:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self.insert(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self.insert(node.right, value)

    def get_sorted(self, node, result):
        if node is not None:
            self.get_sorted(node.left, result)
            result.append(node.data)
            self.get_sorted(node.right, result)

    def sorted_data(self):
        result = []
        self.get_sorted(self.root, result)
        return result
    
    def data(self):
        return self.root
    
# %%
bin = BinarySearchTree([8, 13, 21, 2, 16, 5, 11, 18, 1, 20, 14, 3, 7, 17, 12, 6, 9, 19, 4, 15, 10])

print(bin.sorted_data())
print(bin.data())

# %%
