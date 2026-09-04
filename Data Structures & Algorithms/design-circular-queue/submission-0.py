class Node:
    def __init__(self, value: int):
        self.value = value
        self.prev = None
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0

        # front <-> ... <-> rear
        self.front = Node(-1)
        self.rear = Node(-1)

        self.front.next = self.rear
        self.rear.prev = self.front

    def enQueue(self, value: int) -> bool: # insert rear element. if success true (not full)
        if self.isFull():
            return False

        node = Node(value)

        prev = self.rear.prev
        next = self.rear

        node.prev = prev
        node.next = next
        prev.next = node
        next.prev = node

        self.size += 1
        return True

    def deQueue(self) -> bool: # del front element. if success return true (not empty)
        if self.isEmpty():
            return False
        
        node = self.front.next

        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

        self.size -= 1
        return True
        

    def Front(self) -> int: # get front item. if empty -1
        if self.isEmpty():
            return -1
        return self.front.next.value
        

    def Rear(self) -> int: # get last item. if empty -1
        if self.isEmpty():
            return -1
        return self.rear.prev.value

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.size == self.capacity:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()