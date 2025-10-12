# kreisförmiges Double Linked List

class node:
    def __init__(self,key,value):
        self.value = value
        self.key = key
        self.prev= None
        self.nextN = None

class LinkedList:
    def __init__(self):
        self.head =None
        self.size = 0

    def insert(self, node, position):
        self.size +=1
        prev = self.head
        if position == 0:
            if self.head == None:
                self.head = node
                node.nextN = None
            else:
                node.nextN = self.head
                self.head = node
            lastNode =self.get_node(self.size-1)
            lastNode.nextN = self.head                                    
        else:
            prev = self.get_node(position-1)
            node.nextN = prev.nextN
            prev.nextN = node
            node.prev = prev 


    def get_node(self,position):
        itr = self.head
        count =0
        while (count < position) and (itr != None):
            itr = itr.nextN
            count +=1
        return itr
    
    def get_with_key(self, key):
        itr = self.head
        while (itr != None):
            if itr.key == key:
                break
            itr = itr.nextN
        return itr

    def delete(self, key):
        node = self.get_with_key(key)
        node.prev.next = node.next
        node.next.prev = node.prev
        node = None 

    def print(self):
        if self.size != 0:
            itr = self.head
            while itr != None:
                print(itr.value)
                itr = itr.nextN

linked = LinkedList()
a = node(1)
# b = node(2)
# d = node(4)
# c = node(3)
# e = node(5)
# f = node(6)


linked.insert(a,0)
# linked.insert(b,0)
# linked.insert(d,0)
# linked.insert(e,0)
# linked.insert(f,0)
# linked.insert(c,5)
# print(linked.get_node(0).value)

#insertion and deletion from beginnig O(1) + dynamoc array don't have to allocate size from the start
