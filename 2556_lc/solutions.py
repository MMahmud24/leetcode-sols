class Solution:
    def isPossibleToCutPath(self, grid: list[list[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        if m < 2:
            if n > 2:
                return True
            else:
                return False

        def dfs(i,j):
            if i >= m or j >= n or grid[i][j] == 0:
                return False
            if i == m - 1 and j == n - 1:
                return True

            grid[i][j] = 0
            return dfs(i+1,j) or dfs(i,j+1)


        if not dfs(0,0):
            return True
    
        grid[0][0] = 1
        return not dfs(0,0)


'''
1 1 1 0 0
1 0 1 0 0
1 1 1 1 1
0 0 1 1 1 
0 0 1 1 1 

''
