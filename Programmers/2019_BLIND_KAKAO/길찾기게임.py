class Node:
    def __init__(self,data,idx):
        self.data = data
        self.idx = idx
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.pre_order_lst = []
        self.post_order_lst = []

    def setRoot(self,data,idx):
        self.root = Node(data,idx)

    def insert(self,data,idx):
        if self.root is None:
            self.setRoot(data,idx)
        else:
            self._insert_value(self.root,data,idx)

    def _insert_value(self,cur,data,idx):
        if data < cur.data:
            if cur.left:
                self._insert_value(cur.left,data,idx)
            else:
                cur.left = Node(data,idx)
        else:
            if cur.right:
                self._insert_value(cur.right,data,idx)
            else:
                cur.right = Node(data,idx)

    def _pre_order_traverse(self):
        if self.root is not None:
            self._pre_order(self.root)

    def _pre_order(self,cur):
        self.pre_order_lst.append(cur.idx)
        if cur.left is not None:
            self._pre_order(cur.left)
        if cur.right is not None:
            self._pre_order(cur.right)

    def _post_order_traverse(self):
        if self.root is not None:
            self._post_order(self.root)

    def _post_order(self,cur):
        if cur.left is not None:
            self._post_order(cur.left)
        if cur.right is not None:
            self._post_order(cur.right)
        self.post_order_lst.append(cur.idx)


def solution(nodeinfo):
    answer = [[]]
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    new_nodeinfo = sorted(nodeinfo, reverse=True, key=lambda x:x[1])

    bst = BinarySearchTree()
    for i,lst in enumerate(new_nodeinfo):
        bst.insert(lst[0],lst[2])
    bst._pre_order_traverse()
    bst._post_order_traverse()
    answer = [bst.pre_order_lst,bst.post_order_lst]
    return answer

ex1 = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(ex1))