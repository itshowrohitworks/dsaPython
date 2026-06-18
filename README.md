# DSA with Python:

# 1. Custom Dynamic Array Implementation

A lightweight Python implementation of a **Dynamic Array** built from scratch using fixed-size lists. This project demonstrates how dynamic resizing, memory allocation, and array shifting work.

## Features
```
* **Dynamic Resizing:** 
* **Standard List Operations:** 
* **Boundary Handling:**
```

---

## Time Complexity Analysis

| Operation | Method | Time Complexity | Description |
| :--- | :--- | :--- | :--- |
| **Append** | `append(item)` | $O(1)$ amortized | Fast insertion at the end; occasionally $O(n)$ when resizing. |
| **Prepend** | `prepend(item)` | $O(n)$ | Requires shifting all existing elements to the right. |
| **Insert** | `insert_in_array(index, value)` | $O(n)$ | Shifts elements to the right from the target index. |
| **Delete** | `delete_at_index(index)` | $O(n)$ | Shifts elements to the left and handles memory downscaling. |
| **Print** | `print_array()` | $O(n)$ | Iterates through active elements to display them. |

---

## Code Usage Example

python:

```
# Initialize the dynamic array
myarray = DynamicArray()

# Append elements
myarray.append(5)
myarray.append(6)
myarray.append(7)
myarray.append(8)

# Insert at a specific index
myarray.insert_in_array(4, 3)

# Delete from an index
deleted_value = myarray.delete_at_index(1) # Removes '6'

# Prepend an element to the front
myarray.prepend(19)

# Display final array state
myarray.print_array()
print(f"Size: {myarray.size}, Capacity: {myarray.capacity}")
```

# 2. Hashmaps: Most Imp DS
- in python: dict, sets, Counter, defaultdict all rely on hashing.

## Why we need hashtables?
- instead of using array, linear search which takes O(n), hash takes O(1) avg lookup.

## Hash Function: hash(key)
- python internally converts keys into integer.
- index choosing: index = hash(key) % table_size

## Python Dict:
```
- fruit = {
    "apple":10
}
- access: fruit["apple"] -> 10 (O(1) avg complexity)

- insert: fruit["banana"] = 5

- delete: del fruit["banana"]
```