from doubleLLNode import Node

class DoublyLinkedListHeadTail:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def prepend(self,data):
        new = Node(data)

        if not self.head:
            self.head = new
            self.tail = new
            return
        
        new.next = self.head
        self.head.prev = new
        self.head = new

    def append(self,data):
        new = Node(data)

        if not self.head:
            self.head = new
            self.tail = new
            return
    
        new.prev = self.tail
        self.tail.next = new # type:ignore
        self.tail = new

    def remove(self):
        if not self.head:
            print("Linked List is empty!")
            return
        
        if self.head == self.tail:
            removed = self.head.data
            self.head = None
            self.tail = None
            return removed
        
        removed = self.head.data
        self.head = self.head.next
        self.head.prev = None # type:ignore
        return removed

    def pop(self):
        if not self.head:
            print("Linked List is empty!")
            return
        
        if self.head == self.tail:
            removed = self.head.data
            self.head = None
            self.tail = None
            return removed
        
        removed = self.tail.data # type:ignore
        self.tail = self.tail.prev # type:ignore
        self.tail.next = None # type:ignore
        return removed

    def search(self,value):
        if not self.head:
            print("Linked List is empty!")
            return
        curr = self.head
        while curr:
            if curr.data == value:
                return True
            curr = curr.next
        return False

    def reverse_ll(self):
        if not self.head:
            print("Linked List is empty!")
            return
        
        curr = self.head
        while curr:
            temp = curr.next
            curr.next = curr.prev
            curr.prev = temp

            curr = curr.prev

        self.tail,self.head = self.head,self.tail
        

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

    def reverse_print_ll(self):
        if not self.head:
            print("Linked List is empty!")
            return
        curr = self.tail
        nodes = []
        nodes.append("None")
        while curr:
            nodes.append(str(curr.data))
            curr = curr.prev
        nodes.append("None")
        print(" <-> ".join(nodes))


l = DoublyLinkedListHeadTail()


print(f"Removed from head: {l.remove()}")
print(f"Removed from end: {l.pop()}")

l.prepend(5)
l.prepend(6)
l.prepend(7)

print("\nDLL: ")
l.print_linkedlist()


print(f"\nRemoved from head: {l.remove()}")
print(f"Removed from end: {l.pop()}")

print("\nDLL: ")
l.print_linkedlist()

l.prepend(8)
l.prepend(9)
l.prepend(10)
l.prepend(11)

print("\nDLL: ")
l.print_linkedlist()

print(f"\nRemoved from head: {l.remove()}")
print(f"Removed from end: {l.pop()}")

print("\nDLL: ")
l.print_linkedlist()

l.append(1)
l.append(2)
l.append(3)
l.append(4)

print("\nDLL: ")
l.print_linkedlist()

print(f"\nSearch for 2: {l.search(2)}")
print(f"Search for 10: {l.search(20)}")

print("\nReverse DLL print: ")
l.reverse_print_ll()

print("\nTesting Reverse:")
l.reverse_ll()
print("DLL: ")
l.print_linkedlist()