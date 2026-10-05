class Node:
    def __init__(self, val=0, key=0, prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.items = {}
        self.start = Node()
        self.end = Node()
        self.start.next, self.end.prev = self.end, self.start
        self.capacity = capacity

    def append(self, key, value):
        n = Node(value, key, self.end.prev, self.end)
        self.end.prev.next = n
        self.end.prev = n
        self.items[key] = n

    def pop(self):
        remove = self.start.next
        if remove != self.end:
            self.start.next = remove.next
            remove.next.prev = self.start
            del self.items[remove.key]

    def remove(self, key):
        n = self.items[key]
        n.prev.next = n.next
        n.next.prev = n.prev
        del self.items[n.key]

    def get(self, key: int) -> int:
        if key not in self.items:
            return -1
        n = self.items[key]
        self.remove(n.key)
        self.append(n.key, n.val)
        return n.val

    def put(self, key: int, value: int) -> None:
        if key in self.items:
            self.items[key].val = value
            self.remove(key)
            self.append(key, value)

        elif len(self.items) < self.capacity:
            # put at end and add to map
            self.append(key, value)

        else:
            # remove first element from list and map
            self.pop()
            # put node at end and in map
            self.append(key, value)




        
