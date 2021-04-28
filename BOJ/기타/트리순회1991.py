class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = self.checkNone(left)
        self.right = self.checkNone(right)

    def checkNone(self, ch):
        if ch == '.':
            return None
        else: return ch

    def __str__(self):
        return self.data


class Tree:
    def __init__(self):
        self.root = 'A'

    def preorder(self, node):
        print(node, end='')
        if node.left != None: self.preorder(node_dict[node.left])
        if node.right != None: self.preorder(node_dict[node.right])
        return

    def inorder(self, node):
        if node.left != None: self.inorder(node_dict[node.left])
        print(node, end='')
        if node.right != None: self.inorder(node_dict[node.right])
        return

    def postorder(self, node):
        if node.left != None: self.postorder(node_dict[node.left])
        if node.right != None: self.postorder(node_dict[node.right])
        print(node, end='')
        return


N = int(input())
node_dict = {}
for _ in range(N):
    data, left, right = input().split()
    node = Node(data, left, right)
    node_dict[data] = node

tree = Tree()
tree.preorder(node_dict['A'])
print()
tree.inorder(node_dict['A'])
print()
tree.postorder(node_dict['A'])