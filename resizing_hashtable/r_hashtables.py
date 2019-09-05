

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        # pass
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * capacity

# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    # pass
    hash = 5381
    for s in string:
        hash = ((hash << 5) + hash) + ord(s)

    return hash % max


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    # pass
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] is not None:
        if hash_table.storage[index].key != key:
            print(
                f"WARNING: Overwriting key: {hash_table.storage[index].key}.")
            hash_table.storage[index].key = key
        hash_table.storage[index].value = value
    else:
        hash_table.storage[index] = LinkedPair(key, value)

def hash_table_remove(hash_table, key):
    # pass
    index = hash(key, hash_table.capacity)
    # If you try to remove a value that isn't there, print a warning.
    if hash_table.storage[index] is None or hash_table.storage[index].key != key:
        print(f"Warning: key: {key} does not exist")
    else:
        # else remove the key/value pair
        hash_table.storage[index] = LinkedPair(None, None)

def hash_table_retrieve(hash_table, key):
    # pass
    index = hash(key, len(hash_table.storage))
    if hash_table.storage[index] is not None and hash_table.storage[index].key == key:
        return hash_table.storage[index].value
    else:
        return None

def hash_table_resize(hash_table):
    # make new hashtable with the hashtable function double the capacity
    new_hash_table = HashTable(hash_table.capacity*2)
    for x in range(0, hash_table.capacity):
        if hash_table.storage[x] is not None:
            hash_table_insert(new_hash_table, hash_table.storage[x].key, hash_table.storage[x].value)
            while hash_table.storage[x].next is not None:
                hash_table_insert(new_hash_table, hash_table.storage[x].next.key, hash_table.storage[x].next.value)
                hash_table.storage[x].next = hash_table.storage[x].next.next



def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")
    print("Resized hash table from ")


Testing()
