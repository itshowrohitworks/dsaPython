from typing import Optional

class TreeNode:
    def __init__(self,data) -> None:
        self.data = data
        self.right: Optional[TreeNode] = None
        self.left: Optional[TreeNode] = None

root = TreeNode(10)
b = TreeNode(5)
c = TreeNode(20)
d = TreeNode(2)
e = TreeNode(7)


root.left = b
root.right = c

b.left = d
b.right = e

print(f"Root Node: {id(root)}")
print(f"Root left and b pointing to same memory: {id(root.left) == id(b)}")
print(f"Root right and c pointing to same memory: {id(root.right) == id(c)}")