from singlyLLnode import Node

class SinglyLinkedListHeadTail:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def prepend(self,data): # O(1)
        new = Node(data)
        if not self.head:
            self.head = new
            self.tail = new
            return
        
        new.next = self.head
        self.head = new

    def append(self,data): # O(1)
        new = Node(data)

        if not self.head:
            self.head = new
            self.tail = new
            return
        
        self.tail.next = new # type:ignore
        self.tail = new

    def remove(self): # O(1)
        if not self.head:
            print("Linked List is empty!")
            return
        if self.head == self.tail:
            removed = self.head
            self.head = None
            self.tail = None
            return removed.data # type:ignore
        
        removed = self.head.data # type:ignore
        self.head = self.head.next # type:ignore

        return removed
    
    def pop(self): # O(n)
        if not self.head:
            print("Linked List is empty!")
            return
        
        if self.head == self.tail:
            removed = self.head.data # type:ignore
            self.head = None
            self.tail = None
            return removed
        
        curr = self.head
        while curr.next.next: # type:ignore
            curr = curr.next # type:ignore
        removed = curr.next.data # type:ignore
        curr.next = None # type:ignore
        self.tail = curr
        return removed
    
    def search(self,target): # O(n)
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
            print("Linked List is empty!")
            return
        
        curr = self.head
        nodes = []

        while curr:
            nodes.append(str(curr.data))
            curr = curr.next
        
        nodes.append("None")

        print(" -> ".join(nodes))


l = SinglyLinkedListHeadTail()


print(f"Removed from head: {l.remove()}")
print(f"Removed from end: {l.pop()}")

print(f"\nSize of LinkedList: {l.size()}")

l.append(1)
l.append(2)
l.append(3)
l.append(4)

print(f"\nSize of LinkedList: {l.size()}")
print("Linked List: ",end="")
l.print_linkedlist()

l.prepend(5)
l.prepend(6)
l.prepend(7)
l.prepend(8)

print(f"\nSize of LinkedList: {l.size()}")
print("Linked List: ",end="")
l.print_linkedlist() 

print(f"\nRemoved from head: {l.remove()}")
print(f"Removed from end: {l.pop()}")
print(f"Removed from end: {l.pop()}")

print(f"\nSize of LinkedList: {l.size()}")
print("Linked List: ",end="")
l.print_linkedlist() 

print(f"\nSearch for 5: {l.search(5)}")
print(f"Search for 9: {l.search(9)}")