from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        col = len(board[0])
        parent = list(range(row * col + 1))
        dummy = row * col

        def find(idx):
            if idx != parent[idx]:
                idx = find(parent[idx])
            return idx

        def union(idx1, idx2):
            p1 = find(idx1)
            p2 = find(idx2)

            if p1 == dummy:
                parent[p2] = p1
            else:
                parent[p1] = p2

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'X':
                    continue
                if i == 0 or j == 0 or i == row - 1 or j == col - 1:
                    union(dummy, i * col + j)
                cur = i * col + j
                if j > 0 and board[i][j - 1] == 'O':
                    union(cur - 1, cur)
                if i > 0 and board[i - 1][j] == 'O':
                    union(cur - col, cur)

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O' and find(i * col + j) != dummy:
                    board[i][j] = 'X'

        print(board)

def test_solve():
    solution = Solution()

    assert solution.solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]) == [
        ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]], 'wrong result'


if __name__ == '__main__':
    test_solve()
