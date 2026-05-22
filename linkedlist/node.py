from typing import Optional
class Node:
    def __init__(self,value) -> None:
        self.data = value
        self.next:Optional["Node"] = None

first = Node(1)
second = Node(2)
third = Node(3)

first.next = second
second.next = third

for i in range(5):
    print(first.next.data - i + 1)