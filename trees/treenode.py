from typing import Optional

class BinaryTreeNode:
    def __init__(self,data) -> None:
        self.data = data
        self.right: Optional[BinaryTreeNode] = None
        self.left: Optional[BinaryTreeNode] = None

root = BinaryTreeNode(10)
b = BinaryTreeNode(5)
c = BinaryTreeNode(20)
d = BinaryTreeNode(2)
e = BinaryTreeNode(7)


root.left = b
root.right = c

b.left = d
b.right = e

print(f"Root Node: {id(root)}")
print(f"Root left and b pointing to same memory: {id(root.left) == id(b)}")
print(f"Root right and c pointing to same memory: {id(root.right) == id(c)}")