from doubleLLNode import Node

class DoublyLinkedListHead:

    def __init__(self) -> None:
        self.head = None

    def prepend(self,data):
        new = Node(data)

        if not self.head:
            self.head = new
            return
        
        new.next = self.head
        self.head.prev = new
        self.head = new

    def append(self,data):
        new = Node(data)

        if not self.head:
            self.head = new
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        new.prev = curr
        curr.next = new

    def remove(self):
        if not self.head:
            print("Linked List is empty!")
            return
        removed = self.head.data
        self.head = self.head.next
        return removed
    
    def pop(self):
        if not self.head:
            print("Linked List is empty!")
            return
        if not self.head.next:
            removed = self.head.data
            self.head = None
            return removed
        curr = self.head
        while curr.next.next: # type:ignore
            curr = curr.next # type:ignore
        removed = curr.next.data # type:ignore
        curr.next = None # type:ignore
        return removed
    
    def deleteNode(self,node):
        if not self.head or not node:
            print("Linked List is empty!")
            return
        if node is None:
            return None
        
        if self.head == node:
            self.head = node.next

        if node.next is not None:
            node.next.prev = node.prev
        
        if node.prev is not None:
            node.prev.next = node.next

        node.next = None
        node.prev = None

        return node.data

    def size(self):
        if not self.head:
            return 0
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def print_linkedlist(self):
        if not self.head:
            print("Linked List is empty!")
            return
        curr = self.head
        nodes = []
        nodes.append("None")
        while curr:
            nodes.append(str(curr.data))
            curr = curr.next
        nodes.append("None")
        print(" <-> ".join(nodes))

l = DoublyLinkedListHead()

print(f"Size of DLL: {l.size()}\n")

print(f"Removed at head: {l.remove()}")
print(f"Removed at end: {l.pop()}")

l.append(1)
l.append(2)
l.append(77)

print("\nDoubly Linked List: ")
l.print_linkedlist()
print(f"Size of DLL: {l.size()}")

target = l.head.next # type:ignore
print(f"\nTarget node to delete: {target.data}") # type:ignore
print(f"Removed node: {l.deleteNode(target)}")

print(f"\nRemoved at end: {l.pop()}")

l.append(3)
l.append(4)

print("\nDoubly Linked List: ")
l.print_linkedlist()
print(f"Size of DLL: {l.size()}")

l.prepend(5)
l.prepend(6)
l.prepend(7)
l.prepend(8)


print("\nDoubly Linked List: ")
l.print_linkedlist()
print(f"Size of DLL: {l.size()}")

print(f"\nRemoved at head: {l.remove()}")
print(f"Removed at end: {l.pop()}")
print(f"Removed at end: {l.pop()}")

print("\nDoubly Linked List: ")
l.print_linkedlist()
print(f"Size of DLL: {l.size()}")

target = l.head.next.next # type:ignore
print(f"\nTarget node to delete: {target.data}") # type:ignore
print(f"Removed node: {l.deleteNode(target)}")

print("\nDoubly Linked List: ")
l.print_linkedlist()
print(f"Size of DLL: {l.size()}")