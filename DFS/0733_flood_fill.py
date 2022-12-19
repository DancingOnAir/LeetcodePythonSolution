from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        seen = set()

        def dfs(r, c, o):
            if r < 0 or r >= m or c < 0 or c >= n or (r, c) in seen or image[r][c] != o:
                return
            image[r][c] = color
            seen.add((r, c))
            for dr, dc in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                dfs(r + dr, c + dc, o)

        dfs(sr, sc, image[sr][sc])
        return image


def test_flood_fill():
    solution = Solution()
    assert solution.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]], 'wrong result'
    assert solution.floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 0) == [[0, 0, 0], [0, 0, 0]], 'wrong result'


if __name__ == '__main__':
    test_flood_fill()
