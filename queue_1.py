#queue Umsetzung mit Linked list

from linked_list import *

class Queue:
    def __init__(self):
        self.linkedList = LinkedList()
    
    def enque(self, item):
        current = node(item)
        self.linkedList.insert(current,self.linkedList.size)
    
    def deque(self, item):
        if self.linkedList.size ==0:
            return None
        
        self.linkedList.delete(0)

    def print(self):
        self.linkedList.print()

queue = Queue()
queue.enque(5)
queue.enque(6)
queue.enque(7)
queue.print()

