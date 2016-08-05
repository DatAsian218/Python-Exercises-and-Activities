"""
    7/11/16
    Stacks, Queues, LinkedLists

"""

class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def push(self, add):
        self.stack.append(add)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

"""
aStack = Stack()
print(aStack)

aStack.push(1)
print(aStack)

aStack.size()
print(aStack)
"""

class Queue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return str(self.queue)

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        if (self.size()== 0):
            return True
        else:
            return False

"""
aQueue = Queue()

aQueue.enqueue(1)
print(aQueue)

aQueue.enqueue(2)
print(aQueue)

aQueue.dequeue()
print(aQueue)

print(aQueue.size())
print(aQueue.isEmpty())
"""