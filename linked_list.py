class node:
    def __init__(self,value,key=0):
        self.value = value
        self.key = key
        self.nextN = None

class LinkedList:
    def __init__(self):
        self.head =None
        self.size = 0

    def insert(self, node, position):
        self.size +=1
        prev = self.head
        if position == 0:
            if self.head ==None:
                self.head = node
                node.nextN = None
            else:
                node.nextN = self.head
                self.head = node                        
        else:
            prev = self.get_node(position-1)
            node.nextN = prev.nextN
            prev.nextN = node 


    def get_node(self,position):
        itr = self.head
        count =0
        while (count < position) and (itr != None):
            itr = itr.nextN
            count +=1
        return itr
    
    
    def get_with_key(self,key):
        itr = self.head
        count =0
        while (itr != None):
            if itr.key == key:
                break
            itr = itr.nextN
            count+=1
        return itr,count
            

    def print(self):
        if self.size != 0:
            itr = self.head
            while itr != None:
                print(itr.value)
                itr = itr.nextN
    
    def delete(self, index):
        node = self.get_node(index)
        if index != 0:
            prev = self.get_node(index-1)
            prev.nextN = node.nextN
        node.nextN = None
        self.size-=1
    
    def delete_with_key(self, key):
        if self.size != 0:
            _,index = self.get_with_key(key)
            self.delete(index)



# linked = LinkedList()
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
# linked.print()

#insertion and deletion from beginnig O(1) + dynamoc array don't have to allocate size from the start
# a = node(1,1)
# b = node(2,1)
# d = node(4,1)
# c = node(3,1)
# # e = node(5)
# # f = node(6)


# linked.insert(a,0)
# linked.insert(b,0)
# linked.insert(b,0)
# linked.insert(d,0)
# linked.print()