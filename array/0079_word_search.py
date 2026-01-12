from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        if not m:
            return False
        n = len(board[0])

        def backtrack(i, j, idx):
            char = board[i][j]
            if char != word[idx]:
                return False

            if idx == len(word) - 1:
                return True

            board[i][j] = ''
            for x, y in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                if 0 <= i + x < m and 0 <= j + y < n and backtrack(i + x, j + y, idx + 1):
                    return True

            board[i][j] = char
            return False

        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
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
