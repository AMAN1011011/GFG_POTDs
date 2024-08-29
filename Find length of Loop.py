class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        #Your code here
        s = f = head
        while f and f.next:
            s = s.next
            f = f.next.next
            if s==f:
                count = 1
                while s.next!=f:
                    count+=1
                    s=s.next
                return count
        return 0