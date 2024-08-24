#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val):
       
        # code here
        N = len(wt)
        dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]
        
        for i in range(1, N + 1):
            for w in range(1, W + 1):
                if wt[i - 1] <= w:
                    dp[i][w] = max(dp[i - 1][w], val[i - 1] + dp[i - 1][w - wt[i - 1]])
                else:
                    dp[i][w] = dp[i - 1][w]
        
        return dp[N][W]
