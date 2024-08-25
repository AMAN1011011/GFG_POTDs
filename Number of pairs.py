#User function Template for python3
from bisect import bisect_left, bisect_right
class Solution:
    
     #Function to count number of pairs such that x^y is greater than y^x.     
    def countPairs(self,arr,brr):
        #code here
        ans = 0
        brr.sort()
        
        for x in arr:
            if x == 1:
                continue
            elif x == 2:
                ans += bisect_right(brr, 1)  # upper_bound equivalent in Python
                ans += len(brr) - bisect_left(brr, 5)  # lower_bound equivalent in Python
            else:
                ans += len(brr) - bisect_left(brr, x + 1)
                ans += bisect_right(brr, 1) - bisect_left(brr, 1)  # Counting y == 1
            
            if x == 3:
                ans += bisect_right(brr, 2) - bisect_left(brr, 2)  # Counting y == 2 for x == 3
        
        return ans