#User function Template for python3

class Solution:
	def nthStair(self,n):
		# Code here
		val = 0
        for i in range(0, n+1, 2):
            val += 1
        return val