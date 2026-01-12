from typing import List
from collections import Counter


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        def gcd(a, b):
            return a if b == 0 else gcd(b, a%b)

        ratio = Counter()
        res = 0
        for rect in rectangles:
            s = gcd(rect[0], rect[1])
            w = rect[0] // s
            h = rect[1] // s

            if (w, h) in ratio:
                res += ratio[(w, h)]
            ratio[(w, h)] += 1
        return res

    def interchangeableRectangles1(self, rectangles: List[List[int]]) -> int:
        c = Counter()
        for rec in rectangles:
            c[rec[1] / rec[0]] += 1

        res = 0
        for val in c.values():
            res += val * (val - 1) // 2
        return res


def test_interchangeable_rectangles():
    solution = Solution()

    assert solution.interchangeableRectangles([[4, 8], [3, 6], [10, 20], [15, 30]]) == 6, 'wrong result'
    assert solution.interchangeableRectangles([[4, 5], [7, 8]]) == 0, 'wrong result'


if __name__ == '__main__':
    test_interchangeable_rectangles()
