#User function Template for python3

'''
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

#Function to convert a binary tree to doubly linked list.
class Solution:
    def __init__(self):

        self.prev = None 
        self.head = None 
        
    def bToDLL(self,root):
        def convert_to_dll(node):
            if not node:
                return

            convert_to_dll(node.left)

            if self.prev is None:
                self.head = node

            else:
                node.left = self.prev
                self.prev.right = node
            self.prev = node
            convert_to_dll(node.right)
        convert_to_dll(root)

        return self.head