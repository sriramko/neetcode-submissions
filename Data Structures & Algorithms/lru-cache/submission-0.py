class LRUCache:
    class Node:
        def __init__(self, key, val) -> None:
            self.key, self.val = key, val
            self.prev = self.next = None

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} #maps key to Node

        self.least, self.most = self.Node(0,0), self.Node(0,0) #dummy nodes to ensure nodes on either side always
        self.least.next, self.most.prev = self.most, self.least

    def remove(self, node): #remove any node
        before, after = node.prev, node.next
        before.next, after.prev = after, before

    def insert(self, node): #insert into rightmost
        before, after = self.most.prev, self.most
        before.next = after.prev = node
        node.prev, node.next = before, after

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = self.Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            #remove and evict least recently used from linked list and hashmap
            lru = self.least.next
            self.remove(lru)
            del self.cache[lru.key]
