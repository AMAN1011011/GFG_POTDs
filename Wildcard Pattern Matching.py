# your task is to complete this function
# function should return True/False or 1/0
# str1: pattern
# str2: text
class Solution:
    def wildCard(self,pattern, string):
        # Code here
        n = len(pattern)
        m = len(string)
        dp = [[0] * (m + 2) for _ in range(n + 2)]
        dp[n][m] = 1

        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                if i < n and j < m and (pattern[i] == string[j] or pattern[i] == '?'):
                    dp[i][j] |= dp[i + 1][j + 1]
                if i < n and pattern[i] == '*':
                    dp[i][j] |= dp[i + 1][j + 1]
                    dp[i][j] |= dp[i][j + 1]
                    dp[i][j] |= dp[i + 1][j]

        return dp[0][0] == 1