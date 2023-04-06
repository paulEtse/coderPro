from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    self.mark(grid, i, j)
                    count += 1
        return count

    def mark(self, grid: List[List[str]], i: int, j: int) -> None:
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "1":
            return
        grid[i][j] = "#"
        self.mark(grid, i, j - 1)
        self.mark(grid, i, j + 1)
        self.mark(grid, i + 1, j)
        self.mark(grid, i - 1, j)
