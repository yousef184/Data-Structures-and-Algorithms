# Double Linked List

class node:
    def __init__(self,value=0,key=0):
        self.value = value
        self.key = key
        self.prev= None
        self.nextN = None

class LinkedList:
    def __init__(self):
        self.head =None
        self.top = None
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
                self.head.prev = node
                self.head = node                                 
        else:
            prev = self.get_node(position-1)
            node.prev = prev
            node.nextN = prev.nextN
            prev.nextN = node
            

    def get_prev(self,node):
        print(node.prev.value)

    def get_node(self,position):
        itr = self.head
        count =0
        while (count < position) and (itr != None):
            itr = itr.nextN
            count +=1
            # print(count)
        return itr
    
    def get_with_key(self, key):
        itr = self.head
        while (itr != None):
            if itr.key == key:
                break
            itr = itr.nextN
        return itr

    def delete(self,position):
        if self.size != 0:
            node = self.get_node(position)
            if position ==0:
                self.head = None
            if node.prev:
                node.prev.nextN = node.nextN
                # print(1)
            if node.nextN:
                print(node.nextN.prev.value)
                node.nextN.prev = None
            self.size -=1

    def delete_with_key(self, key):
        if self.size != 0:
            node = self.get_with_key(key)
            if node.prev:
                node.prev.nextN = node.nextN
            if node.nextN:
                node.nextN.prev = node.prev
            self.size -=1
    
    

    def print(self):
        if self.size != 0:
            itr = self.head
            while itr != None:
                print(itr.value, end=" ")
                itr = itr.nextN

linked = LinkedList()
# a = node(1)
# b = node(2)
# d = node(4)
# c = node(3)
# e = node(5)
# f = node(6)


# linked.insert(a,0)
# linked.insert(b,0)
# linked.insert(d,0)
# linked.insert(e,0)
# linked.insert(f,0)
# linked.insert(c,5)
# linked.get_prev(c)

# linked.insert(e,0)
# linked.insert(f,0)
# linked.insert(c,5)
# print(linked.get_node(0).value)
# linked.delete(2)
# linked.print()
#insertion and deletion from beginnig O(1) + dynamoc array don't have to allocate size from the start
