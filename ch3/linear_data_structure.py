class Stack:
    """Implementation of the stack abstract data type."""
    
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return not self.items
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)


class Queue:
    """Implementation of the queue abstract data type where the rear is at
    position 0 of the list.
    """
    
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return not self.items
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)


class EndRearQueue(Queue):
    """Implementation of the queue abstract data type where the rear is at
    the end of the list.
    """
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0)


class Deque:
    """Implementation of the deque abstract data type, where the rear of
    the deque is at position 0.
    """
    
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return not self.items
    
    def add_front(self, item):
        self.items.append(item)
    
    def add_rear(self, item):
        self.items.insert(0, item)
    
    def remove_front(self):
        return self.items.pop()
    
    def remove_rear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)