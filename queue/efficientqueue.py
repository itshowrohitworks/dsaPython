from collections import deque
class EfficientQueue:

    def __init__(self) -> None:
        self.items = deque()
    
    def enqueue(self,value):
        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty!")
        return self.items.popleft()
    
    def is_empty(self):
        return (len(self.items) == 0)

    def front(self):
        if self.is_empty():
            return None
        return self.items[0]

    def size(self):
        return len(self.items)

    # to prevent queue from printing raw deque object:
    def print_queue(self):
        if self.is_empty():
            print(f"Queue is empty!")
            return
        print(list(self.items))

q = EfficientQueue()

# q.dequeue() -> Index Error here!

print(f"Front of Queue: {q.front()}")
print(f"Size of Queue: {q.size()}")

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print("\nQueue: ",end="")
q.print_queue()

q.dequeue()
q.dequeue()

print("\nQueue: ",end="")
q.print_queue()

print(f"\nFront of Queue: {q.front()}")
print(f"Size of Queue: {q.size()}")