#User function Template for python3
class Solution:
    
    # Note that the size of the array is n-1
    def missingNumber(self, n, arr):
        # code here
        total = n*(n+1)/2
        arrsum = sum(arr)
        missing = int(total-arrsum)
        return missing