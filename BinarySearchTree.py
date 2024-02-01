class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)

        else:
            new_node = Node(data)
            current = self.root
            while True:
                if(new_node.data < current.data):
                    if(current.left == None):
                        current.left = new_node
                        break
                    else:
                        current = current.left

                elif(new_node.data > current.data):
                    if(current.right == None):
                        current.right = new_node
                        break
                    else:
                        current = current.right

                else: 
                    print(data," Already exists!")

    def lookup(self,data):
        current = self.root
        if(self.root == None):
            print("Tree is Empty!")
        else:
            while(current):
                if(data < current.data):
                    current = current.left

                elif(data > current.data):
                    current = current.right                        
                
                elif(data == current.data):
                    return print(data," Exists!")
                    

            return print(data," Doesnt Exist!")

    def remove(self,data):
        if(self.root == None):
            return print("Tree is Empty!")
        else:
            current_node = self.root
            parent_node = current_node
            while(current_node):
                if(data < current_node.data):
                    parent_node = current_node
                    current_node = current_node.left

                elif(data > current_node.data):
                    parent_node = current_node
                    current_node = current_node.right

                elif(data == current_node.data):
                    #Deleting Leaf Node
                    if(current_node.left == None and current_node.right == None):
                        if(parent_node.left == current_node):
                            parent_node.left = None
                            print("Deleted Leaf Node: ", current_node.data)
                            del current_node
                            return
                        else:
                            parent_node.right = None
                            print("Deleted Leaf Node: ", current_node.data)
                            del current_node
                            return
                    
                    #Deleting Node with One Child
                    if(current_node.left == None or current_node.right == None):
                        if(current_node.right == None): #If left link has a child
                            parent_node.left = current_node.left
                            print("Deleted Node With One Child: ", current_node.data)
                            del current_node
                            return
                        else: #If right link has a child
                            parent_node.right = current_node.right
                            print("Deleted Node With One Child: ", current_node.data)
                            del current_node
                            return

                    #Deleting Node with Two Children
                    if(current_node.left != None and current_node.right != None):
                        succesor = current_node.right
                
                        if(succesor.left!=None):
                            while(succesor.left != None):
                                parent_succesor = succesor
                                succesor = succesor.left
                            parent_succesor.left = None

                        if(parent_node.left == current_node):
                            parent_node.left = succesor
                        elif(parent_node.right == current_node):
                            parent_node.right = succesor

                        succesor.left = current_node.left
                        if(succesor != current_node.right): #If successor is adj node
                            succesor.right = current_node.right

                        
                        if(current_node == self.root):#If Root
                            self.root = succesor

                        print("Deleted Node With Two Children: ", current_node.data)
                        del current_node
                        return
                
                else:
                    print("Node Doesnt Exist!")   
                    return  

    def traverse(self, traversing_node):
        inorder_array = []

        def inorder(traversing_node):
            if(traversing_node == None):
                return
            else:
                inorder(traversing_node.left)
                inorder_array.append(traversing_node.data)
                inorder(traversing_node.right)
                
        inorder(traversing_node)
        print("Inorder Traversal: ", inorder_array)
        del inorder_array

        
            




new_bst = BST()
new_bst.insert(10)
new_bst.insert(5)
new_bst.insert(20)
new_bst.insert(15)
new_bst.insert(25)
new_bst.insert(3)
new_bst.insert(30)
new_bst.insert(8)
new_bst.insert(7)
new_bst.insert(9)
new_bst.lookup(15)
new_bst.lookup(7)
new_bst.lookup(14)
new_bst.traverse(new_bst.root)
new_bst.remove(10)
new_bst.remove(5)
new_bst.remove(25)
new_bst.traverse(new_bst.root)
