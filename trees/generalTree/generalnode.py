from typing import Optional

class GeneralNode:
    def __init__(self, data):
        self.data = data
        self.children = []


g = GeneralNode(5)

a = GeneralNode(6)
b = GeneralNode(7)

g.children.append(a)
g.children.append(b)

print(f"G: {g.data}")
print(f"G's:{g.data} Children Nodes: {[i.data for i in g.children]}")