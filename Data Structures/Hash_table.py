from linked_list import *

class HashTable:
    MAXSIZE = 10
    def __init__(self, array = []):
        self.size = HashTable.MAXSIZE
        self.array = [LinkedList() for i in range(self.size)]

    def __setitem__(self,key,value):
        if isinstance(key,str):
            index = HashTable.hashfunc(key)
        elif isinstance(key,int):
            index = index%HashTable.MAXSIZE
        else:
            return 0
        varNode = node(value,key) 
        self.array[index].insert(varNode,0)
        # print(self.array[index].get_with_key(key).value)
        
    def __getitem__(self,key):
        index = HashTable.hashfunc(key)
        if self.array[index].size > 1:
            node,_= self.array[index].get_with_key(key)
            return node.value
        if self.array[index].get_node(0) != None:
            return self.array[index].get_node(0).value
    
    def __delitem__(self,key):
        index = HashTable.hashfunc(key)
        if self.array[index].size > 1:
            self.array[index].delete_with_key(key)
        else:
            self.array[index] = LinkedList()

    @staticmethod
    def hashfunc(string):
        sum = 0
        for c in string:
            sum += ord(c)
        return sum%10

a = HashTable()
a["march"]="aloo"
a["balloon"] = "hallo"
a["samy"] = "lamy"
# print(a.array[0].head.value)
print(a["samy"])
print(a["balloon"])
print(a["march"])
del a["samy"]
print(a["samy"])
del a["balloon"]
print(a["march"])



#look up by key is O(1) and Insertion deletion is O(1)