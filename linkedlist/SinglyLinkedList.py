from singlyLLnode import Node

class SinglyLinkedListHead:
    def __init__(self) -> None:
        self.head = None
    
    def prepend(self,data):
        new = Node(data)

        new.next = self.head
        self.head = new

    def append(self,data):
        new = Node(data)
        if not self.head:
            self.head = new
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        
        curr.next = new
    
    def remove(self):
        if not self.head:
            print("Linked List is Empty!")
            return
        removed = self.head
        self.head = self.head.next
        return removed.data
    
    def pop(self):
        if not self.head:
            print("Linked List is Empty!")
            return
        
        # only one node in the list:
        if not self.head.next:
            removed = self.head
            self.head = None
            return removed.data
        
        curr = self.head
        while curr.next.next: # type:ignore
            curr = curr.next # type:ignore
        removed = curr.next # type:ignore
        curr.next = None # type:ignore
        return removed.data # type:ignore
    
    def search(self,target):
        if not self.head:
            print("Linked List is empty!")
            return
        curr = self.head
        while curr:
            if curr.data == target:
                return True
            curr = curr.next
        return False
    
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
            print("Linked List is Empty!")
            return
        current = self.head
        nodes = []
        
        while current:
            nodes.append(str(current.data))
            current = current.next
            
        nodes.append("None")
        
        print(" -> ".join(nodes))


l = SinglyLinkedListHead()

l.pop()

print(f"\nSize of SLL: {l.size()}")
l.prepend(5)
l.prepend(6)

print(f"\nSize of SLL: {l.size()}")
print("Linked List: ",end="")
l.print_linkedlist()

l.append(1)
l.append(2)
l.append(3)
l.append(4)

print(f"\nSize of SLL: {l.size()}")
print("Linked List: ",end="")
l.print_linkedlist()

print(f"\nRemoved at head: {l.remove()}")
print(f"Removed at end: {l.pop()}")

print(f"\nSize of SLL: {l.size()}")
print("Linked List: ",end="")
l.print_linkedlist()
print(f"\nIs 7 in the list: {l.search(7)}")
print(f"\nIs 5 in the list: {l.search(5)}")