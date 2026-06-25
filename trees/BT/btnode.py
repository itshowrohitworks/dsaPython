from typing import Optional

class BTNode:
    def __init__(self,data) -> None:
        self.value = data
        self.right: Optional[BTNode] = None
        self.left: Optional[BTNode] = None


a = BTNode(10)
b = BTNode(5)
c = BTNode(20)
d = BTNode(2)
e = BTNode(7)

a.left = b
a.right = c

b.left = d
b.right = e

print(f"a.left and b points to same memory: {(id(a.left) == id(b))}")
print(f"a.right and c points to same memory: {(id(a.right) == id(c))}")
print(f"b.left and d points to same memory: {(id(b.left) == id(d))}")
print(f"b.right and e points to same memory: {(id(b.right) == id(e))}")