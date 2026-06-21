from typing import Optional

class Node:
    def __init__(self,value) -> None:
        self.data = value
        self.prev:Optional["Node"] = None
        self.next:Optional["Node"] = None

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)


a.next = b
b.prev = a

b.next = c
c.prev = b

a.prev = d
d.next = a