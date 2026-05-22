class HashTable:
    def __init__(self,size=10) -> None:
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self,key):
        return hash(key) % self.size
    
    def __setitem__(self,key,value):
        index = self._hash(key)

        bucket = self.table[index]

        for i,(k,v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key,value)
                return
        bucket.append((key,value))

    def __getitem__(self,key):
        index = self._hash(key)

        bucket = self.table[index]

        for k,v in bucket:
            if k == key:
                return v
        raise KeyError(key)
    
    def __delitem__(self,key):
        index = self._hash(key)

        bucket = self.table[index]

        for i,(k,v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
        raise KeyError(key)
    
    # Tasks:
    def __contains__(self,key):
        index = self._hash(key)
        bucket = self.table[index]

        for k,v in bucket:
            if k == key:
                return True
        return False

    def keys(self):
        all_keys = []
        for bucket in self.table:
            for k,v in bucket:
                all_keys.append(k)
        return all_keys
    
    def values(self):
        all_values = []
        for bucket in self.table:
            for k,v in bucket:
                all_values.append(v)
        return all_values
    
    def items(self):
        key_value = []
        for bucket in self.table:
            for k,v in bucket:
                key_value.append((k,v))
        return key_value

    def print_table(self):
        print("{")
        for k in self.table:
            print(k)
        print("}")

# Testing:
my_hash = HashTable()

# 1. Triggers __setitem__
my_hash["apple"] = 5
my_hash["banana"] = 12
my_hash["orange"] = 55

# 2. Triggers __contains__ (and runs in O(1) time!)
if "apple" in my_hash:
    print("Yes, we have apples!")

# 3. Triggers __getitem__
print(my_hash["apple"])  # Output: 5

# 4. Gather data using your clean list-returns
print(my_hash.keys())    # Output: ['apple', 'banana'] (order depends on hash bucket)
print(my_hash.values())  # Output: [5, 12]
print(my_hash.items())   # Output: [('apple', 5), ('banana', 12)]

print("\nCustom HashTable Structure:")
my_hash.print_table()
# 5. Triggers __delitem__
del my_hash["apple"]