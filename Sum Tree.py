#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    def is_sum_tree(self, node):
        # code here
        
        def f(node):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return node.data
            val = f(node.left) + f(node.right)
            if val == node.data:
                return 2 * val
            return -1
        
        if node is None:
            return True
        return f(node) != -1