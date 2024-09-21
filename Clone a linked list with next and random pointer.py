#User function Template for python3

'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.random=None
        
param: head:  head of linkedList to copy
return: the head of the copied linked list the #output will be 1 if successfully copied
'''
class Solution:
    #Function to clone a linked list with next and random pointer.
    def copyList(self, head):
        # code here
        if not head:
            return None
            
        d = {}
        curr = head
        
        while curr:
            d[curr]=Node(curr.data)
            curr=curr.next
            
        curr=head
        while curr:
            d[curr].next=d.get(curr.next)
            d[curr].random=d.get(curr.random)
            curr=curr.next
            
        return d[head]