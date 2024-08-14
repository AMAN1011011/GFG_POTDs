#User function Template for python3

class Solution:
    def longestCommonSubstr(self, str1, str2):
        # code here
        n = len(str1)
        m = len(str2)
        dp = [[0] * (m + 1) for _ in range(2)]
        maxLength = 0
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i % 2][j] = dp[(i - 1) % 2][j - 1] + 1
                    maxLength = max(maxLength, dp[i % 2][j])
                else:
                    dp[i % 2][j] = 0
        
        return maxLength
