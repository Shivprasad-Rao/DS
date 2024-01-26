class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def enqueue(self,data):
        if self.length == 0:
            new_node = Node(data)
            self.first = self.last = new_node
        else:
            new_node = Node(data)
            self.last.next = new_node
            self.last = new_node
        self.length+=1
    
    def dequeue(self):
        if self.length == 0:
            print("Queue is Empty")
        elif self.length == 1:
            print("Dequeued Node Value: ",self.first.data)
            self.first = None
            self.last = None
            self.length -= 1
        else:
            current_node = self.first
            print("Dequeued Node Value: ",current_node.data)
            self.first = current_node.next
            self.length-=1
            del current_node

    def peek(self):
        if self.length==0:
            return ("Queue is Empty")
        else:
            print(self.first.data)

    def printList(self):
        if self.length == 0:
            print('Queue is Empty')
        else:
            valueArray = []
            current_node = self.first
            valueArray.append(current_node.data)
            while(current_node.next != None): 
                current_node = current_node.next
                valueArray.append(current_node.data)
            print(valueArray)

new_queue = Queue()
new_queue.enqueue(10)
new_queue.enqueue(20)
new_queue.enqueue(30)
new_queue.enqueue(40)
new_queue.printList()
new_queue.peek()
new_queue.dequeue()
new_queue.peek()
new_queue.dequeue()
new_queue.printList()
new_queue.peek()
new_queue.dequeue()
new_queue.peek()
new_queue.dequeue()
new_queue.printList()