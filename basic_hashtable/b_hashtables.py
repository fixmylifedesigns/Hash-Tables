

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        # pass
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * self.capacity

# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''


def hash(string, max):
    hash = 5381
    for s in string:
        hash = ((hash << 5) + hash) + ord(s)

    return hash % max

        # hash = 0
    # for i in string :
    #     hash += ord(i)
    # return hash % max


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
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
        hash_table.storage[index] = Pair(key, value)


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
        # hash the key, max is hash table capacity
    index = hash(key, hash_table.capacity)
    # If you try to remove a value that isn't there, print a warning.
    if hash_table.storage[index] is None or hash_table.storage[index].key != key:
        print(f"Warning: key: {key} does not exist")
    else:
        # else remove the key/value pair
        hash_table.storage[index] = Pair(None, None)


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, len(hash_table.storage))
    if hash_table.storage[index] is not None and hash_table.storage[index].key == key:
        return hash_table.storage[index].value
    else:
        return None


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
