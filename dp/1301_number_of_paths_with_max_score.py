class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        MOD = 10**9 + 7
        n = len(board)
        max_sum = [[float('-inf')] * (n + 1) for _ in range(n + 1)]
        ways = [[0] * (n + 1) for _ in range(n + 1)]
        max_sum[0][0] = 0
        ways[0][0] = 1

        for i in range(n):
            for j in range(n):
                if board[i][j] == 'X':
                    continue
                max_sum[i+1][j+1] = s = max(max_sum[i][j], max_sum[i+1][j], max_sum[i][j+1])
                if max_sum[i][j] == s:
                    ways[i+1][j+1] += ways[i][j]
                if max_sum[i+1][j] == s:
                    ways[i+1][j+1] += ways[i+1][j]
                if max_sum[i][j+1] == s:
                    ways[i+1][j+1] += ways[i][j+1]
                ways[i+1][j+1] %= MOD
                if board[i][j].isdigit():
                    max_sum[i+1][j+1] += int(board[i][j])
        return [max_sum[-1][-1], ways[-1][-1]] if max_sum[-1][-1] != float('-inf') else [0, 0]


def test_paths_with_max_score():
    solution = Solution()
    assert solution.pathsWithMaxScore(["E23","2X2","12S"]) == [7,1], 'wrong result'
    assert solution.pathsWithMaxScore(["E12","1X1","21S"]) == [4,2], 'wrong result'
    assert solution.pathsWithMaxScore(["E11","XXX","11S"]) == [0,0], 'wrong result'


if __name__ == '__main__':
    test_paths_with_max_score()
