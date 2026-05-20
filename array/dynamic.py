class DynamicArray:

    def __init__(self) -> None:
        self.capacity = 1
        self.size = 0
        self.arr = [None] * self.capacity

    def resize(self):
        self.capacity *= 2

        new_arr = [None] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]
        
        self.arr = new_arr

    def append(self,item):
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = item
        self.size += 1

    def prepend(self,item):
        if self.size == self.capacity:
            self.resize()
        if self.size == 0:
            self.arr[self.size] = item
            self.size += 1
            return
        for i in range(self.size - 1,-1,-1):
            self.arr[i + 1] = self.arr[i]
        self.arr[0] = item
        self.size += 1                

    def print_array(self):
        if self.size == 0:
            print("Array is empty")
            return
        elements = []
        for i in range(self.size):
            elements += [str(self.arr[i])]
        print("[" + ",".join(elements) + "]")

    def insert_in_array(self,index,value):
        if index < 0 or index > self.size:
            raise IndexError("Index is out of range!")
        
        if self.size == self.capacity:
            self.resize()
        
        for i in range(self.size - 1,index - 1,-1):
            self.arr[i + 1] = self.arr[i]
        self.arr[index] = value
        self.size += 1

    def delete_at_index(self,index):
        if index < 0 or index >= self.size:
            raise IndexError("Index is out of range!")
        if self.size == 0:
            return "Empty Array!"
        temp = self.arr[index]
        for i in range(index,self.size-1):
            self.arr[i] = self.arr[i + 1]
        self.arr[self.size - 1] = None
        self.size -= 1
        # Shrink capacity only if the array is 1/4 used:
        if self.size > 0 and self.size <= self.capacity // 4:
            self.capacity = self.capacity // 2
            self.arr = [self.arr[i] for i in range(self.capacity)]
        return temp

myarray = DynamicArray()
myarray.append(5)
myarray.append(6)
myarray.append(7)
myarray.append(8)
print(f"Array:",end="")
myarray.print_array()
print(f"Size of Array: {myarray.size}")
print(f"Capacity of Array: {myarray.capacity}")

print("\n")

myarray.insert_in_array(4,3)
print(f"Array:",end="")
myarray.print_array()
print(f"Size of Array: {myarray.size}")
print(f"Capacity of Array: {myarray.capacity}")

print("\n")

print(myarray.delete_at_index(1))
print(f"Array:",end="")
myarray.print_array()
print(f"Size of Array: {myarray.size}")
print(f"Capacity of Array: {myarray.capacity}")

myarray.append(22)
myarray.append(48)
myarray.append(99)
myarray.append(15)

print("\n")

myarray.prepend(19)
print(f"Array:",end="")
myarray.print_array()
print(f"Size of Array: {myarray.size}")
print(f"Capacity of Array: {myarray.capacity}")