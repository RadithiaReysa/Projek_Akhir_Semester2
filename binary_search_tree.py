class BSTNode:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, nim, nama):
        if root is None:
            return BSTNode(nim, nama)
        
        if nim < root.nim:
            root.left = self.insert(root.left, nim, nama)

        else:
            root.right = self.insert(root.right, nim, nama)
        return root

    def search(self, root, nim):
        if root is None:
            return None
        
        if root.nim == nim:
            return root

        if nim < root.nim:
            return self.search(root.left, nim)
        
        return self.search(root.right, nim)