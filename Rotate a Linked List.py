# Your task is to complete this function

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        # code here
        if head is None or k == 0:
            return head
        
        start = None
        end = head
        p = head
        length = 1
        while end.next is not None:
            if length == k:
                start = end
            end = end.next
            length += 1
        
        k = k % length
        if start is None or k == 0:
            return head
        head = start.next
        start.next = None
        end.next = p
        
        return head
