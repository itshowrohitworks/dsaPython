class Queue:

    def __init__(self) -> None:
        self.items = []

    def enqueue(self,value):
        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty!")
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        return (len(self.items) == 0)
    
    def size(self):
        return len(self.items)
    
q = Queue()

# q.dequeue() -> Index Error here!

print(f"Front of Queue: {q.front()}")
print(f"Size of Queue: {q.size()}")

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print(f"\nQueue: {q.items}")

q.dequeue()
q.dequeue()

print(f"Queue: {q.items}")
print(f"\nFront of Queue: {q.front()}")
print(f"Size of Queue: {q.size()}")