class Node:
    def __init__(self, value):
        self.data = value
        self.nxt = None

    def __repr__(self):
        print("Value:", self.data," Next:", self.nxt)
        
class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def appendNode(self,value):
        new_node = Node(value)
        self.tail.nxt = new_node
        self.tail = new_node
        self.length += 1

    def prependNode(self, value):
        new_node = Node(value)
        new_node.nxt = self.head
        self.head = new_node
        self.length += 1

    def printList(self):
        LinkedListData = []
        currentNode = self.head
        while(currentNode!=None):
            LinkedListData.append(currentNode.data)
            currentNode=currentNode.nxt
        print(LinkedListData)

    def insertAt(self,index,value):
        if index==0:
            self.prependNode(value)
        elif index >= self.length-1:
            self.appendNode(value)
        else:
            i=0
            currentNode = self.head
            while(i<index-1):
                currentNode = currentNode.nxt
                i+=1
            nextNode = currentNode.nxt
            newNode = Node(value)
            currentNode.nxt = newNode
            newNode.nxt = nextNode
            self.length += 1

    def deleteNode(self,index):
        if index == 0:
            nextNode = self.head.nxt
            del self.head
            self.head = nextNode
            
        elif index >= self.length-1:
            lastNode = self.head
            while(lastNode.nxt != None):
                prevNode = lastNode
                lastNode = lastNode.nxt
            prevNode.nxt = None 
            self.tail = prevNode
            del lastNode

        else:
            i=0
            currentNode = self.head
            prevNode = currentNode
            if(index == 1):
                currentNode = currentNode.nxt
            else:    
                while(i<index):
                    prevNode = currentNode
                    currentNode = currentNode.nxt
                    i += 1
            prevNode.nxt = currentNode.nxt
            del currentNode

        self.length -= 1

    def reverse(self):
        revArray = []

        currentNode = self.head
        while(currentNode.nxt != None):
            revArray.append(currentNode.data)
            currentNode = currentNode.nxt
            self.length -= 1
        revArray.append(currentNode.data)
        self.length -= 1

        self.head.data = revArray.pop()
        self.tail = self.head
        self.length = 1
        currentNode = self.head
        while(len(revArray) != 0):
            currentNode = currentNode.nxt
            currentNode.data = revArray.pop()
            self.tail = currentNode
            self.length += 1

    def reverseBetterMethod(self):
        if(self.head.nxt == None):
            return
        else:
            prevNode = self.head
            currentNode = self.head.nxt
            nextNode = currentNode
            prevNode.nxt = None
            self.tail = prevNode
            while(currentNode!=None):
                nextNode = currentNode.nxt
                currentNode.nxt = prevNode
                prevNode = currentNode
                self.head = prevNode
                currentNode = nextNode


newList = LinkedList(10)
newList.appendNode(5)
newList.appendNode(20)
newList.prependNode(4)
newList.insertAt(2,7)
newList.insertAt(3,8)
newList.insertAt(2,17)
newList.insertAt(3,18)
newList.printList()

print("\n---Deleting Nodes---")
newList.deleteNode(0)
newList.printList()

newList.deleteNode(10)
newList.printList()

newList.deleteNode(2)
newList.printList()

print("\n---Reverse---")
newList.reverseBetterMethod()
newList.printList()

# print("\n---Reverse---")
# newList.reverse()
# newList.printList()

