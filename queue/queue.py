"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


class Queue1:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def enqueue(self, value):
        """
        add to head
        """
        if value:
            self.storage.insert(0, value)
            self.size += 1

    def dequeue(self):
        """
        remove from tail
        """
        if self.size > 0:
            self.size -= 1
            return self.storage.pop()


class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        """
        add value to tail
        """
        new_node = Node(value)
        # empty list
        n = self.head
        if not n:
            self.head = new_node
            return
        # non-empty list
        while n.get_next():
            n = n.get_next()
        n.set_next(new_node)

    def remove(self):
        """
        remove value from head
        """
        # empty list
        if not self.head:
            return None
        n = self.head.get_value()
        # non-empty list
        self.head = self.head.get_next()
        return n


class Queue2:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        """
        add to back
        """
        if value is not None:
            self.storage.add(value)
            self.size += 1

    def dequeue(self):
        if self.size > 0:
            ret = self.storage.remove()
            self.size -= 1
            return ret


Queue = Queue2

if __name__ == "__main__":
    q = Queue()
