from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # m: 세로, n: 가로
        m, n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]

        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]

        def dfs(cy, cx):
            visited[cy][cx] = 1

            for i in range(4):
                ny = cy + dy[i]
                nx = cx + dx[i]

                if 0 <= ny <= m - 1 and 0 <= nx <= n - 1:
                    if grid[ny][nx] == "1" and visited[ny][nx] != 1:
                        dfs(ny, nx)

        count = 0
        for v in range(m):
            for w in range(n):
                if grid[v][w] == "1" and visited[v][w] != 1:
                    dfs(v, w)
                    count += 1

        return count


if __name__ == '__main__':
    s = Solution()
    # 섬은 물로 둘러싸여있다.
    # 섬은 1, 물은 0이다.
    # 섬의 개수를 구한다: connected component를 구한다.
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(s.numIslands(grid))
