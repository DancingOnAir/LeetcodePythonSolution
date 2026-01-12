from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        res = 0
        stk = [-1]
        heights.append(0)
        for i in range(len(heights)):
            while heights[stk[-1]] > heights[i]:
                h = heights[stk.pop()]
                w = i - stk[-1] - 1
                res = max(res, w * h)
            stk.append(i)
        heights.pop()

        return res


def test_largest_rectangle_area():
    solution = Solution()

    heights1 = [2, 1, 5, 6, 2, 3]
    print(solution.largestRectangleArea(heights1))

    heights2 = [1, 1]
    print(solution.largestRectangleArea(heights2))


if __name__ == '__main__':
    test_largest_rectangle_area()
