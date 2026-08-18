from typing import List


class Solution:
    def largestRectangleArea1(self, heights: List[int]) -> int:
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

    def largestRectangleArea(self, heights: list[int]) -> int:
        if not heights:
            return 0

        n = len(heights)
        left = [-1] * n
        right = [n] * n
        stk = []
        for i, h in enumerate(heights):
            while stk and heights[stk[-1]] > h:
                right[stk.pop()] = i

            if stk:
                left[i] = stk[-1]
            stk.append(i)

        res = 0
        for h, l, r in zip(heights, left, right):
            res = max(res, h * (r - l - 1))
        return res

def test_largest_rectangle_area():
    solution = Solution()
    assert solution.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10, "wrong result"
    assert solution.largestRectangleArea([2, 4]) == 4, "wrong result"


if __name__ == '__main__':
    test_largest_rectangle_area()
