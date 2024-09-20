#User function Template for python3

class Solution:
    # Returns count buildings that can see sunlight
    def countBuildings(self, height):
        # code here
        if not height:
            return 0
        
        ans = 1
        maxh = height[0]
        for i in range(1, len(height)):
            if height[i]>maxh:
                ans +=1
                maxh = height[i]
        return ans