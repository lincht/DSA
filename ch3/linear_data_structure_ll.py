from list_ import UnorderedList


class Stack:
    """Implementation of the stack abstract data type using linked lists."""
    
    def __init__(self):
        self.items = UnorderedList()
    
    def is_empty(self):
        return self.items.is_empty()
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        
        previous = None
        current = self.items.head
        
        while current is not None:
            previous = current
            current = current.get_next()
        
        return previous.get_data()
    
    def size(self):
        return self.items.length()


class Queue:
    """Implementation of the queue abstract data type using linked lists."""
    
    def __init__(self):
        self.items = UnorderedList()
    
    def is_empty(self):
        return self.items.is_empty()
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return self.items.length()


class Deque:
    """Implementation of the deque abstract data type using linked lists, where
    the rear of the deque is at position 0.
    """
    
    def __init__(self):
        self.items = UnorderedList()
    
    def is_empty(self):
        return self.items.is_empty()
    
    def add_front(self, item):
        self.items.append(item)
    
    def add_rear(self, item):
        self.items.insert(0, item)
    
    def remove_front(self):
        return self.items.pop()
    
    def remove_rear(self):
        return self.items.pop(0)
    
    def size(self):
        return self.items.length()