from typing import List
from collections import defaultdict


min = lambda a, b: b if b < a else a
max = lambda a, b: b if b > a else a


class Solution:
    def maxArea(self, coords: List[List[int]]) -> int:
        res = 0

        def calc() -> None:
            min_x, max_x = float('inf'), 0
            min_y = defaultdict(lambda: float('inf'))
            max_y = defaultdict(int)
            for x, y in coords:
                min_x = min(min_x, x)
                max_x = max(max_x, x)
                min_y[x] = min(min_y[x], y)
                max_y[x] = max(max_y[x], y)

            nonlocal res
            for x, y in min_y.items():
                res = max(res, (max_y[x] - y) * max(max_x - x, x - min_x))

        calc()
        for p in coords:
            p[0], p[1] = p[1], p[0]

        calc()
        return res or -1

    def maxArea1(self, coords: List[List[int]]) -> int:
        xs = defaultdict(list)
        ys = defaultdict(list)
        for x, y in coords:
            xs[x].append(y)
            ys[y].append(x)

        def helper(m: defaultdict[List]):
            if len(m) < 2:
                return -1
            sorted_key = sorted(m.keys())
            res = -1
            for k, v in m.items():
                if len(v) < 2:
                    continue
                d = max(v) - min(v)
                res = max(res, d * max(k - sorted_key[0], sorted_key[-1] - k))
            return res

        return max(helper(xs), helper(ys))


def test_max_area():
    solution = Solution()
    assert solution.maxArea([[1, 1], [1, 2], [3, 2], [3, 3]]) == 2, 'wrong result'
    assert solution.maxArea([[1, 1], [2, 2], [3, 3]]) == -1, 'wrong result'


if __name__ == '__main__':
    test_max_area()
