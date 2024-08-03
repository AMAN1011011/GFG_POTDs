
class Solution:
    def celebrity(self, mat):
        n = len(mat)
        m = len(mat[0])
        for i in range(n):
            row = 0
            col = 0
            for j in range(m):
                if mat[i][j] == 0:
                    row += 1
                if mat[j][i] == 1:
                    col += 1
            if row == n and col == n - 1:
                return i
        return -1