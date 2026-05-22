# DSA with Python:

# 1. Hashmaps: Most Imp DS
- in python: dict, sets, Counter, defaultdict all rely on hashing.

## Why we need hashtables?
- instead of using array, linear search which takes O(n), hash takes O(1) avg lookup.

## Hash Function: hash(key)
- python internally converts keys into integer.
- index choosing: index = hash(key) % table_size

## Python Dict:
- fruit = {
    "apple":10
}
- access: fruit["apple"] -> 10 (O(1) avg complexity)

- insert: fruit["banana"] = 5

- delete: del fruit["banana"]