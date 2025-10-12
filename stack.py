#Ein Stack könnte mit Liste gemacht wird, es ist jedoch sehr uneffiktive, weil die ganze liste kopiert wird. Es wird auch Ram-Speicherplatz Verschwendung geben.

#Eine Stack-Umsetzung mit Double Linked List
from double_linked_list import *

class Stack:
    def __init__(self):
        self.stackLinked= LinkedList()
    
    def pop(self):
        if self.stackLinked.size == 0:
            return None
        item = self.stackLinked.get_node(self.stackLinked.size-1)
        self.stackLinked.delete(self.stackLinked.size-1)
        return item

    def push(self,item):
        current = node(item)
        self.stackLinked.top = current
        self.stackLinked.insert(current,self.stackLinked.size)
        pass

    def stack_top_element(self):
        print(self.stackLinked.top.value)

    def print(self):
        self.stackLinked.print()

stack = Stack()
stack.push("allooo")
# stack.push(2)
# stack.push(3)

# # stack.pop()
# # stack.pop()
# # stack.pop()
# # stack
stack.print()
# stack.stack_top_element()

#another way to implement the stack is using deque
# from collections import deque
