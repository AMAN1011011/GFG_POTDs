#User function Template for python3
import heapq
from typing import List

# User function Template for python3
class Solution:
    # Function to return the minimum cost of connecting the ropes.
    def minCost(self, arr: List[int]) -> int:
        heapq.heapify(arr)
        
        ans = 0
        
        while len(arr) > 1:
            j = heapq.heappop(arr)
            k = heapq.heappop(arr)
            
            su = j + k
            ans += su
            
            heapq.heappush(arr, su)
        
        return ans