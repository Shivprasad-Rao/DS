class Node:
    def __init__(self, value):
        self.data = value
        self.nxt = None
        self.prev = None

    def __repr__(self):
        print("Value:", self.data," Next:", self.nxt)
        
class DoublyLinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def appendNode(self,value):
        new_node = Node(value)
        self.tail.nxt = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1

    def prependNode(self, value):
        new_node = Node(value)
        new_node.nxt = self.head
        self.head.prev = new_node
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
            newNode.prev = currentNode
            newNode.nxt = nextNode
            nextNode.prev = newNode
            self.length += 1

    def deleteNode(self,index):
        if index == 0:
            nextNode = self.head.nxt
            del self.head
            self.head = nextNode
            
        elif index >= self.length-1:
            lastNode = self.tail
            prevNode = self.tail.prev
            prevNode.nxt = None 
            del lastNode

        else:
            i=0
            currentNode = self.head
            if(index == 1):
                currentNode = currentNode.nxt
            else:    
                while(i<index):
                    currentNode = currentNode.nxt
                    i += 1
            prevNode = currentNode.prev
            nextNode = currentNode.nxt
            prevNode.nxt = nextNode
            nextNode.prev = prevNode
            del currentNode

        self.length -= 1


newList = DoublyLinkedList(10)
newList.appendNode(5)
newList.appendNode(20)
newList.prependNode(4)
newList.insertAt(2,7)
newList.insertAt(3,8)
newList.printList()
newList.deleteNode(0)
newList.printList()
newList.deleteNode(10)
newList.printList()
newList.deleteNode(2)
newList.printList()
