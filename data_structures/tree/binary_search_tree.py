class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def _insert(node, value):
            if not node:
                return TreeNode(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node
        
        self.root = _insert(self.root, value)
        
    def inorder_transversal(self):
        def _inorder(node):
            return _inorder(node.left) + [node.value] + _inorder(node.right) if node else []
        return _inorder(self.root)
    
    def search(self, value):
        def _search(node, value):
            if not node:
                return False

            if value == node.value:
                return True
            
            elif value < node.value:
                return _search(node.left, value)
            
            else:
                return _search(node.right, value)
        return _search(self.root, value)