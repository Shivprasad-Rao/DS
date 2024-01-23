class Stack:
    def __init__(self):
        self.array = []

    def push(self, data):
        self.array.append(data)

    def pop(self):
        if len(self.array) == 0:
            print("Stack is empty")
        else:
            print("Popped Node Value: ",self.array.pop())
        
    def peek(self):
        if len(self.array) == 0:
            print("Stack is Empty")
        else:
            print("Peek: ",self.array[len(self.array)-1])   

    def printList(self):
        print(self.array)
        
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
