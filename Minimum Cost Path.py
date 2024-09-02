import heapq
class Solution:
    
    #Function to return the minimum cost to react at bottom
	#right cell from top left cell.
	def minimumCostPath(self, grid):
		#Code here
		n = len(grid)
        
        # Maintaining visited array
        vis = [[0] * n for _ in range(n)]
        
        # Priority queue to find the element where we can reach with the least points
        pq = []
        heapq.heappush(pq, (grid[0][0], 0, 0))  # (cost, x, y)
        vis[0][0] = 1
        
        # For checking all the neighbors of a given element
        delx = [1, 0, -1, 0]
        dely = [0, 1, 0, -1]
        
        while pq:
            w, x, y = heapq.heappop(pq)
            
            # If bottom-right element found, break
            if x == n - 1 and y == n - 1:
                return w
            
            for j in range(4):
                tx = x + delx[j]
                ty = y + dely[j]
                
                if 0 <= tx < n and 0 <= ty < n and vis[tx][ty] == 0:
                    # If the element is not yet visited, insert it into the priority queue
                    heapq.heappush(pq, (w + grid[tx][ty], tx, ty))
                    vis[tx][ty] = 1
