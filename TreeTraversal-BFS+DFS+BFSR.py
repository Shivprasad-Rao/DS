#For BFS,
#Dont use this method of popping from the queue because it takes O(n) to dequeue.
#Instead create and use the Data Structure or Import "deque" from collections

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def bfs(self):
        array = []
        queue = []
        queue.append(self.root)
        while(len(queue)!=0):
            current_node = queue.pop(0)#Check head of file
            array.append(current_node.data)
            if(current_node.left):
                queue.append(current_node.left)
            if(current_node.right):
                queue.append(current_node.right)
        return array

    def bfsRecursive(self,queue,array):
        
        if(len(queue)==0):
            return array
        
        while(len(queue)!= 0):
            current_node = queue.pop(0) # O(n), other methods suggested in the head
            array.append(current_node.data)

            if(current_node.left):
                queue.append(current_node.left)
            if(current_node.right):
                queue.append(current_node.right)
            
            return self.bfsRecursive(queue,array)

    

    def dfsInorder(self):

        # Inorder Recursive Function
        def traverseInorder(current_node,array):
            
            if(current_node.left):
                traverseInorder(current_node.left, array)
            
            array.append(current_node.data)

            if(current_node.right):
                traverseInorder(current_node.right,array)

            return array


        return traverseInorder(self.root, [])

    def dfsPreorder(self):

        #Preorder Recursive Function    
        def traversePreorder(current_node,array):
            
            array.append(current_node.data)

            if(current_node.left):
                traversePreorder(current_node.left,array)
            
            if(current_node.right):
                traversePreorder(current_node.right,array)

            return array
        

        return traversePreorder(self.root,[])

    def dfsPostorder(self):

        #Postorder Recursive Function
        def traversePostorder(current_node, array):
            
            if(current_node.left):
                traversePostorder(current_node.left,array)

            if(current_node.right):
                traversePostorder(current_node.right,array)

            array.append(current_node.data)
            return array
        
        
        return traversePostorder(self.root, [])

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

print("Breadth First Search:",new_bst.bfs())
print("Breadth First Search Recursive:",new_bst.bfsRecursive([new_bst.root],[])) #passing a list and passing the queue by putting the root in a list
print("Depth First Search Inorder:", new_bst.dfsInorder())
print("Depth First Search Preorder:", new_bst.dfsPreorder())
print("Depth First Search Postorder:", new_bst.dfsPostorder())

