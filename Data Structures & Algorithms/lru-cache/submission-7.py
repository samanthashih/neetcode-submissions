class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val

        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key : Node(key, val)

        # head <-> lru <-> ... <-> mru <-> tail
        self.head = Node(-1, -1) 
        self.tail = Node(-2, -2) 
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # key moved to mru
        node = self.cache[key]
        print("get: ", node.key)
        self.removeNode(node)
        self.insertNodeTail(node)

        return node.val
        
    def put(self, key: int, value: int) -> None:
        # key moved to mru
        print("put: ", key)
        if key in self.cache: 
            # remove old node
            self.removeNode(self.cache[key])
        
        node = Node(key, value)
        self.cache[key] = node
        self.insertNodeTail(node)

        if len(self.cache) > self.capacity:
            lru = self.head.next
            print("lru: ", lru.key)
            # remove lru
            self.removeNode(lru)
            del self.cache[lru.key]

    def removeNode(self, node: Node):
        prev = node.prev
        next = node.next
        # print("remove node: ", node.key)
        # print("--- node: ", node.key)
        # print("--- node.prev: ", node.prev.key)
        # print("--- node.next: ", node.next.key)

        prev.next = next
        next.prev = prev
    
    def insertNodeTail(self, node: Node):
        prev = self.tail.prev
        next = self.tail

        prev.next = node
        node.prev = prev

        node.next = next
        next.prev = node
        
        print("--- node: ", node.key)
        print("--- node.prev: ", node.prev.key)
        print("--- node.next: ", node.next.key)