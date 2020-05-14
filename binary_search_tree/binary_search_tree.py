"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value > self.value:
            # we head right
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
        elif value < self.value:
            # we head left
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        elif value == self.value:
            # duplicates
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
            return self

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # at start, root is self
        # compare target with value
        if target == self.value:
            return True
        if target < self.value:
            # go left
            if not self.left:
                return False
            return self.left.contains(target)
        if target > self.value:
            # go right
            if not self.right:
                return False
            return self.right.contains(target)
            # Return the maximum value found in the tree

    def get_max(self):
        if self.right:
            return self.right.get_max()
        return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
        return fn(self.value)  # every leaf calls fn on itself.
    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            # depth first
            self.left.in_order_print(node)
        print(self.value)
        if self.right:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        # node is parent
        print(node.value)
        # parent left, parent right,
        if node.left:
            self.left.bft_print(node.left)
        if node.right:
            self.right = node.right
            self.right.bft_print(node.right)
        # left child.bft, right child.bft

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
