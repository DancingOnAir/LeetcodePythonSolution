from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        if not m:
            return False

        n = len(board[0])
        marked = [[False] * n for _ in range(m)]

        def helper(x, y, idx, marked):
            if idx == len(word):
                return True

            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != word[idx] or marked[x][y]:
                return False

            marked[x][y] = True
            if helper(x, y - 1, idx + 1, marked) or \
                    helper(x, y + 1, idx + 1, marked) or \
                    helper(x - 1, y, idx + 1, marked) or \
                    helper(x + 1, y, idx + 1, marked):
                return True
            marked[x][y] = False

        for i in range(m):
            for j in range(n):
                if helper(i, j, 0, marked):
                    return True

        return False


def test_exist():
    solution = Solution()

    board1 = [['A', 'B', 'C', 'E'],
             ['S', 'F', 'C', 'S'],
             ['A', 'D', 'E', 'E']]
    word1 = "ABCCED"
    print(solution.exist(board1, word1))
    word2 = "SEE"
    print(solution.exist(board1, word2))
    word3 = "ABCB"
    print(solution.exist(board1, word3))


if __name__ == '__main__':
    test_exist()
