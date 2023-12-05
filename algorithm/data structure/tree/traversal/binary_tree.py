class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # 전위 순회
    def preorder(self, node):
        if node is not None:
            print(node.data, end=' ')
        if node.left is not None:
            self.preorder(node.left)
        if node.right is not None:
            self.preorder(node.right)

    # 중위 순회
    def inorder(self, node):
        if node is not None:
            if node.left is not None:
                self.inorder(node.left)
            print(node.data, end=' ')
        if node.right is not None:
            self.inorder(node.right)

    # 후위 순회
    def postorder(self, node):
        if node is not None:
            if node.left is not None:
                self.postorder(node.left)
            if node.right is not None:
                self.postorder(node.right)
            print(node.data, end=' ')

    # 레벨 순회
    def levelorder(self, node):
        queue = []
        queue.append(node)
        while queue:
            top = queue.pop(0)
            print(top.data, end=' ')
            if top.left is not None:
                queue.append(top.left)
            if top.right is not None:
                queue.append(top.right)
