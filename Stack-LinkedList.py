class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def push(self, data):
        new_node = Node(data)
        temp_node = self.top
        if self.length == 0:
            self.top = new_node
            self.bottom = self.top
        else:    
            self.top = new_node
            self.top.next = temp_node
        del temp_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            print("Stack is empty")
        elif(self.length == 1):
            print("Popped Node Value: ",self.top.data)
            self.top = None
            self.bottom = self.top
            self.length -= 1
        else:
            print("Popped Node Value: ",self.top.data)
            current_node = self.top
            self.top = current_node.next
            self.length -= 1
            del current_node
        
    def peek(self):
        if self.length == 0:
            print("Stack is Empty")
        else:
            print("Peek: ",self.top.data)   

    def printList(self):
        if self.length == 0:
            print('Stack is Empty')
        else:
            valueArray = []
            current_node = self.top
            valueArray.append(current_node.data)
            while(current_node.next != None): 
                current_node = current_node.next
                valueArray.append(current_node.data)
            print(valueArray[::-1])
        
new_stack = Stack()
new_stack.push(10)
new_stack.push(20)
new_stack.push(30)
new_stack.push(40)
new_stack.printList()
new_stack.peek()
new_stack.pop()
new_stack.peek()
new_stack.pop()
new_stack.peek()
new_stack.pop()
new_stack.peek()
new_stack.pop()
new_stack.printList()