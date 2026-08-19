class Solution:
    # question 0084 solution
    def get_largest_size(self, heights: list[int]) -> int:
        size = 0
        stk = [-1]
        for right, h in enumerate(heights):
            while len(stk) > 1 and heights[stk[-1]] >= h:
                i = stk.pop()
                left = stk[-1]
                # 长和宽取小的那个才能形成正方形
                size = max(size, min(heights[i], right - left - 1))
            stk.append(right)
        return size

    # mono stack solution
    def maximalSquare1(self, matrix: list[list[str]]) -> int:
        n = len(matrix[0])
        heights = [0] * (n + 1)
        res = 0
        for r in matrix:
            # 计算底边为r的柱子高度
            for j, c in enumerate(r):
                if c == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            res = max(res, self.get_largest_size(heights))
        return res * res

    def maximalSquare(self, matrix: list[list[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if col == '1':
                    dp[i + 1][j + 1] = min(dp[i][j], dp[i][j + 1], dp[i + 1][j]) + 1
        return max(map(max, dp)) ** 2


def test_maximal_square():
    solution = Solution()
    assert solution.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]) == 4, 'wrong result'
    assert solution.maximalSquare([["0","1"],["1","0"]]) == 1, 'wrong result'
    assert solution.maximalSquare([["0"]]) == 0, 'wrong result'


if __name__ == '__main__':
    test_maximal_square()

