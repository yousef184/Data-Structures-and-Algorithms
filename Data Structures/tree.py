#heighracl structure

class TreeNode:
    def __init__(self,item=0):
        self.parent = None
        self.children = []
        self.item = item

class Tree:
    def __init__(self):
        self.size = 0
        self.root = None
        pass

    def insert(self,current,parent=None):
        self.size+=1
        current.parent = parent
        if self.size == 1:
            self.root = current
            return
        elif parent != None:
            parent.children.append(current)
        

    def print(self, node):
        if node.item != None:
            print(node.item)
            self.print_child(node)

    
    def print_child(self,node):
        itr = node
        for child in itr.children:
            print(child.item, f"child of {child.parent.item}")
            if len(child.children) > 0:
                self.print_child(child)
        

    def delete(self,node):
        self.size-=1
        for child in node.children:
            self.delete(child)
        node.item = None 
        node.children.clear()
        count = 0
        if node.parent:
            for child in node.parent.children:
                if node.item == child.item:
                    node.parent.children.pop(count)
                count+=1    

# tree = Tree()
# node1= TreeNode(1)
# node2= TreeNode(2)
# node3= TreeNode(3)
# tree.insert(node1)
# tree.insert(node2,node1)
# tree.insert(node3,node1)
# node4= TreeNode(4)
# node5= TreeNode(5)
# tree.insert(node4,node2)
# tree.insert(node5,node2)
# # tree.delete(node3)
# # node1 = None

# tree.print(node1)