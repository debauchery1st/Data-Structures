"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


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


class Stack1:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        if value:
            self.storage.append(value)
            self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.pop()
        return None


class Stack2:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        if value:
            self.storage.add(value)
            self.size += 1

    def pop(self):
        newStore = LinkedList()  # crate a new storage container
        idx = 1  # start pseudo-index at 1
        while idx < (len(self)):
            # add removed elements to newStore
            newStore.add(self.storage.remove())
            idx += 1  # increase pseudo-index
        # newStore includes everything except the last element.
        last_element = self.storage.remove()  # last element from storage
        self.storage = newStore  # switch to the new linked list we created
        if last_element:
            self.size -= 1  # decrease element count
        return last_element  # return the missing element


Stack = Stack1

if __name__ == "__main__":
    soda = Stack2()
    soda.push('cola')
    soda.push('beer of route')
    soda.push('ale of ginger')
    print(soda.pop())
    print(soda.pop())
    print(soda.pop())
