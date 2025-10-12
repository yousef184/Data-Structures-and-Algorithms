# search complexity log2(n) and insertion log2(n)

class BinaryTreeNode:
    def __init__(self,item):
        self.item = item
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root =None
    
    def insert(self,node):
        if self.root == None:
            self.root = node
            return
        if self.search(node.item):
            print("element already exists")
            return 0
        parent = self.root
        self.traverese(node,parent)

    def traverese(self,node,parent):
        if node.item > parent.item:
            if parent.right:
                self.traverese(node, parent.right)
            else:
                parent.right = node
        if node.item  < parent.item:
            if parent.left:
                self.traverese(node, parent.left)
            else:
                parent.left = node
        pass

    def print(self):
        self.post_order(self.root)
            

    def in_order(self,parent):
        if parent == None:
            return
        self.in_order(parent.left)
        print(parent.item)
        self.in_order(parent.right)
    
    def pre_order(self,parent):
        if parent == None:
            return
        print(parent.item)
        self.pre_order(parent.left)
        self.pre_order(parent.right)

    def post_order(self,parent):
        if parent == None:
            return
        self.post_order(parent.left)
        self.post_order(parent.right)
        print(parent.item)


    def delete(self,node):
        if node.right:
            if node.left:
                self.find_max(node)
            else:
                node.item = node.right.item
                node.right =None
        elif node.left:
            node.item = node.left.item
            node.left =None
        else:
            self.delete_node(node)
        pass

    def delete_node(self, node):
        


    def find_max(self,node):
        if parent == None:
        pass
        
    
    def search(self,item):
        parent = self.root 
        if parent.item == item:
           return True
        return self.search_recursive(parent, item)

    def search_recursive(self, parent, item):
        if parent:    
            if item < parent.item:
                result = self.search_recursive(parent.left, item)
            elif item > parent.item:
                result = self.search_recursive(parent.right, item)
            else:
                result = True
            return result

tree = BinaryTree()
a = BinaryTreeNode(1)
b = BinaryTreeNode(2)
c = BinaryTreeNode(-1)
d = BinaryTreeNode(-2)
e = BinaryTreeNode(0.5)
f = BinaryTreeNode(1.5)
g = BinaryTreeNode(3)
tree.insert(a)
tree.insert(b)
tree.insert(c)
tree.insert(d)
tree.insert(e)
tree.insert(f)
tree.insert(g)
# print(tree.search(-2))
# if():
#     print("Not found")


# tree.delete(f)

tree.print()
# print(a.right.item)

