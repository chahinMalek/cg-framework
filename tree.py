from typing import List, Deque
from collections import deque

class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.children = []

    def add_child(self, child) -> None:
        self.children.append(child)

    def add_data(self, data, mode: str="write") -> None:
        if mode == "write":
            self.data = data
        elif mode == "append":
            self.data = list(self.data)
            self.data += list(data)
        else:
            return

    def is_leaf(self) -> bool:
        return not self.children

    def __str__(self) -> str:
        return str(self.data)

    def __repr__(self) -> str:
        return str(self)


class Tree:

    def __init__(self, root: Node) -> None:
        self.root = root

    def depth_first_traversal(self) -> List[Node]:
        nodes_to_visit, visited = list(self.root.children[::-1]), [self.root]

        def _dft(current: Node, stack: List['Node']) ->None:
            if not stack:
                return
            current = stack.pop()
            visited.append(current)
            stack += current.children[::-1]
            _dft(current, stack)

        _dft(self.root, nodes_to_visit)
        return visited

    def breadth_first_traversal(self) -> List[Node]:
        nodes_to_visit, visited = deque(self.root.children), [self.root]

        def _bft(current: Node, queue: Deque['Node']) ->None:
            if not queue:
                return
            current = queue.popleft()
            visited.append(current)
            queue += current.children
            _bft(current, queue)

        _bft(self.root, nodes_to_visit)
        return visited

    def get_nodes(self, algorithm: str="bft") -> List['Node']:
        if algorithm == "bft":
            return self.breadth_first_traversal()
        elif algorithm == "dft":
            return self.depth_first_traversal()
        else:
            return []

    def get_leaf_nodes(self, algorithm: str="bft") -> List['Node']:
        return [node for node in self.get_nodes(algorithm) if node.is_leaf()]

"""
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')
i = Node('i')

a.add_child(b)
a.add_child(f)
b.add_child(c)
b.add_child(d)
b.add_child(e)
f.add_child(g)
f.add_child(h)
f.add_child(i)

t = Tree(a)
leafs = t.get_leaf_nodes()
print(leafs)
"""