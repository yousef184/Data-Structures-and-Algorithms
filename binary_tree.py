# search complexity log2(n) and insertion log2(n)

class BinaryTreeNode:
    def __init__(self,item):
        self.item = item
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root =None
    
    def insert(self,item):
        node = BinaryTreeNode(item)
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


    def delete(self,item):
        node = self.search(item)
        # print(node.item)
        if node.right:
            if node.left:
                max = self.find_max(node.left)
                temp = max.item
                self.delete_node(max)
                node.item = temp
            else:
                node.item = node.right.item
                node.right =None
        elif node.left:
            node.item = node.left.item
            node.left =None
        else:
            # print(node.item)
            self.delete_node(node)
        pass

    def delete_node(self,node):
        parent = self.get_parent(node,self.root)
        # print(parent.item)
        if parent:    
            if parent.left == node:
                parent.left = None
            elif parent.right == node:
                parent.right = None

    def get_parent(self,node,parent):
        if node.item > parent.item:
            if parent.right:
                if node.item != parent.right.item:
                    result = self.get_parent(node, parent.right)
                else:
                    result = parent
        elif node.item < parent.item:
            if parent.left:
                if node.item != parent.left.item:
                    result = self.get_parent(node, parent.left)
                else:
                    result = parent
        return result

    def find_max(self,node):
        if node.right:
            result = self.find_max(node.right)
        else:
            result = node
        return result
        
    
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
                result = parent
            return result
        
    def re(self):
        return 3

tree = BinaryTree()
tree.insert(1)
tree.insert(2)
tree.insert(-1)
tree.insert(-2)
tree.insert(0.5)
tree.insert(1.5)
tree.insert(3)
tree.delete(2)

tree.print()

