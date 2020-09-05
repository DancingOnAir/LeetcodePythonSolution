from typing import List


class Solution:
    def get_largest_rectangle_area(self, heights):
        stk = [-1]
        heights.append(0)
        res = 0
        for i in range(len(heights)):
            while heights[stk[-1]] > heights[i]:
                res = max(res, heights[stk.pop()] * (i - stk[-1] - 1))
            stk.append(i)
        heights.pop()

        return res

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        res = 0
        dp = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[j] = dp[j] + 1 if matrix[i][j] == "1" else 0
            res = max(res, self.get_largest_rectangle_area(dp))
        return res


def test_maximal_rectangle():
    solution = Solution()

    matrix1 = [["1", "0", "1", "0", "0"],
               ["1", "0", "1", "1", "1"],
               ["1", "1", "1", "1", "1"],
               ["1", "0", "0", "1", "0"]]
    print(solution.maximalRectangle(matrix1))

    matrix2 = [["0", "1"],
               ["1", "0"]]
    print(solution.maximalRectangle(matrix2))

if __name__ == '__main__':
    test_maximal_rectangle()
