class Node:
    """
    A class representing a node in a singly linked list.
    Each node contains data and a reference to the next node.
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return str(self.data)


class SinglyLinkedList:
    """
    A class representing a singly linked list.
    The list maintains a reference to the head node.
    """
    def __init__(self):
        self.head = None
        self.size = 0
        
    def isEmpty(self):
        """Check if the list is empty."""
        return self.head is None
        
    def length(self):
        """Return the length of the list."""
        return self.size
    
    def insertAtBeginning(self, data):
        """Insert a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        
    def insertAtEnd(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)
        
        if self.isEmpty():
            self.head = new_node
        else:
            current = self.head
            # Traverse to the last node
            while current.next:
                current = current.next
            current.next = new_node
            
        self.size += 1
        
    def insertAtPosition(self, position, data):
        """Insert a new node at the specified position."""
        if position < 0 or position > self.size:
            raise IndexError("Position out of range")
            
        if position == 0:
            self.insertAtBeginning(data)
            return
            
        new_node = Node(data)
        current = self.head
        
        # Traverse to the node just before the desired position
        for _ in range(position - 1):
            current = current.next
            
        new_node.next = current.next
        current.next = new_node
        self.size += 1
        
    def deleteAtBeginning(self):
        """Delete the node at the beginning of the list."""
        if self.isEmpty():
            raise Exception("Cannot delete from an empty list")
            
        self.head = self.head.next
        self.size -= 1
        
    def deleteAtEnd(self):
        """Delete the node at the end of the list."""
        if self.isEmpty():
            raise Exception("Cannot delete from an empty list")
            
        if self.head.next is None:
            self.head = None
        else:
            current = self.head
            
            # Traverse to the second last node
            while current.next.next:
                current = current.next
                
            current.next = None
            
        self.size -= 1
        
    def deleteAtPosition(self, position):
        """Delete the node at the specified position."""
        if self.is_empty():
            raise Exception("Cannot delete from an empty list")
            
        if position < 0 or position >= self.size:
            raise IndexError("Position out of range")
            
        if position == 0:
            self.deleteAtBeginning()
            return
            
        current = self.head
        
        # Traverse to the node just before the one to be deleted
        for _ in range(position - 1):
            current = current.next
            
        current.next = current.next.next
        self.size -= 1
        
    def search(self, data):
        """Search for a node with the given data and return its position."""
        current = self.head
        position = 0
        
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
            
        return -1  # Data not found
        
    def getAtPosition(self, position):
        """Get the data at the specified position."""
        if position < 0 or position >= self.size:
            raise IndexError("Position out of range")
            
        current = self.head
        
        # Traverse to the desired position
        for _ in range(position):
            current = current.next
            
        return current.data
        
    def update(self, position, data):
        """Update the data at the specified position."""
        if position < 0 or position >= self.size:
            raise IndexError("Position out of range")
            
        current = self.head
        
        # Traverse to the desired position
        for _ in range(position):
            current = current.next
            
        current.data = data
        
    def reverse(self):
        """Reverse the linked list in-place."""
        previous = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
            
        self.head = previous
        
    def display(self):
        """Display the linked list."""
        elements = []
        current = self.head
        
        while current:
            elements.append(str(current.data))
            current = current.next
            
        return " -> ".join(elements) if elements else "Empty list"