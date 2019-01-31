class Node:
    """Building block for the linked list implementation."""
    
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, data):
        self.data = data
    
    def set_next(self, node):
        self.next = node


class UnorderedList:
    """Implementation of the unordered list abstract data type."""
    
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def __str__(self):
        
        items = ''
        current = self.head
        
        while current is not None:
            items += str(current.get_data()) + ', '
            current = current.get_next()
        
        return '[{}]'.format(items[:-2])
    
    def add(self, item):
        """Add a new item to the beginning of the list."""
        
        n = Node(item)
        n.set_next(self.head)
        self.head = n
    
    def length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.get_next()
        
        return count
    
    def search(self, item):
        """Search for the item in the list and returns a boolean value."""
        
        current = self.head
        
        while current is not None:
            if current.get_data() == item:
                return True
            else:
                current = current.get_next()
        
        return False
    
    def remove(self, item):
        """Remove the item from the list. Do nothing if the item is not
        in the list.
        """
        
        previous = None
        current = self.head
        
        while current is not None:
            
            if current.get_data() == item:
                # If the item to be removed is the first item
                if previous is None:
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())
                return
            
            else:
                previous = current
                current = current.get_next()
    
    def append(self, item):
        """Add a new item to the end of the list."""
        
        n = Node(item)
        current = self.head
        
        # Special case - empty list
        if current is None:
            self.head = n
        else:
            # Find the last node
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(n)
    
    def index(self, item):
        """Return the position of the item in the list."""
        
        pos = 0
        current = self.head
        
        while current is not None:
            if current.get_data() == item:
                return pos
            else:
                current = current.get_next()
                pos += 1
        
        raise ValueError('{} is not in list'.format(item))
    
    def insert(self, pos, item):
        """Add a new item to the list at position pos."""
        
        if pos == 0:
            self.add(item)
        
        elif pos >= self.length():
            self.append(item)
        
        else:
            previous = None
            current = self.head
            
            for _ in range(pos):
                previous = current
                current = current.get_next()
            
            n = Node(item)
            previous.set_next(n)
            n.set_next(current)
    
    def pop(self, pos=None):
        """Remove and return the item at position pos. If pos=None, remove and
        return the last item.
        """
        
        if self.is_empty():
            raise IndexError('pop from empty list')
        
        if pos is None:
            pos = self.length() - 1
        
        elif pos >= self.length():
            raise IndexError('pop index out of range')
        
        previous = None
        current = self.head
        
        for _ in range(pos):
            previous = current
            current = current.get_next()
        
        # If the item to be removed is the first item
        if pos == 0:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
        
        return current.get_data()
    
    def slice_(self, start, stop):
        """Return a copy of the list starting at the start position and going
        up to but not including the stop position.
        """
        
        sl = UnorderedList()
        
        current = self.head
        
        for i in range(min(stop, self.length())):
            if i >= start:
                sl.append(current.get_data())
            current = current.get_next()
        
        return sl