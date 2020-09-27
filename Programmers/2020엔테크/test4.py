def solution(t1, t2):
    class Node:
        def __init__(self, item):
            self.data = item
            self.left = None
            self.right = None
            self.parent = None

    class BinaryTree:
        def __init__(self):
            self.root = Node(0)
            self.current = self.root
            self.node_address = [self.root]

        def fill_data(self, lst):
            self.node_address += [-1] * (len(lst)-1)
            for p, tu in enumerate(lst):
                l, r = tu
                parent = self.node_address[p]
                if l != -1:
                    left = Node(l)
                    left.parent = parent
                    parent.left = left
                    self.node_address[l] = left
                if r != -1:
                    right = Node(r)
                    right.parent= parent
                    parent.right = right
                    self.node_address[r] = right

        def find_t2(self, t2):
            cnt = 0
            for start in self.node_address:
                self.current = start
                t2.current = tree2.root
                visited = [False] * len(t2.node_address)
                visited[0] = True
                s = [t2.current]

                is_ans = True
                while s:
                    if t2.current.left and not visited[t2.current.left.data]:
                        if self.current.left:
                            s.append(t2.current.left)
                            visited[t2.current.left.data] = True
                            self.current = self.current.left
                            t2.current = t2.current.left
                            continue
                        else:
                            is_ans = False
                            break
                    elif not t2.current.left and self.current.left:
                        is_ans = False
                        break

                    elif t2.current.right and not visited[t2.current.right.data]:
                        if self.current.right:
                            s.append(t2.current.right)
                            visited[t2.current.right.data] = True
                            self.current = self.current.right
                            t2.current = t2.current.right
                            continue
                        else:
                            is_ans = False
                    elif not t2.current.right and self.current.right:
                        is_ans = False
                        break

                    s.pop(-1)
                    self.current = self.current.parent
                    t2.current = t2.current.parent

                if is_ans:
                    cnt += 1

            return cnt

    tree1 = BinaryTree()
    tree1.fill_data(t1)
    tree2 = BinaryTree()
    tree2.fill_data(t2)

    answer = tree1.find_t2(tree2)

    return answer