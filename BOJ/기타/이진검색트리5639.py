import sys
sys.setrecursionlimit(10**4)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    root = None

    def setRoot(self, root):
        self.root = root

    def insert_node(self, node):
        if self.root == None: self.setRoot(node)
        else: self.search_location(self.root, node)

    def search_location(self, parent, new_node):
        if new_node.data < parent.data:
            if parent.left: self.search_location(parent.left, new_node)
            else: parent.left = new_node
        else:
            if parent.right: self.search_location(parent.right, new_node)
            else: parent.right = new_node

    def postorder(self, node, ans):
        if node.left: ans = self.postorder(node.left, ans)
        if node.right: ans = self.postorder(node.right, ans)
        return ans+[node.data]


bst = BinarySearchTree()

while True:
    try:
        number = int(input())
    except:
        break
    bst.insert_node(Node(number))

answer = bst.postorder(bst.root, [])
for ans in answer:
    print(ans)