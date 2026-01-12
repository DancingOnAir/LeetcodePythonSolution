from typing import List
from collections import Counter


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        c = Counter(changed)
        if c[0] & 1:
            return []

        for x in sorted(c):
            if c[x] > c[x * 2]:
                return []
            c[x * 2] -= c[x] if x else c[x] // 2
        return list(c.elements())

    def findOriginalArray1(self, changed: List[int]) -> List[int]:
        if len(changed) & 1:
            return []

        res = list()
        c = {k: v for k, v in sorted(Counter(changed).items(), key=lambda x: x[0])}
        for k, v in c.items():
            if v <= 0:
                continue

            if k * 2 not in c or v > c[k * 2]:
                return []

            if not k:
                if v & 1:
                    return []
                c[k] = 0
                res += [k] * (v // 2)
            else:
                c[k] -= v
                c[k * 2] -= v
                res += [k] * v
        return res


def test_find_original_array():
    solution = Solution()

    assert solution.findOriginalArray([2, 1]) == [1], 'wrong result'
    assert solution.findOriginalArray([0, 0, 0, 0]) == [0, 0], 'wrong result'
    assert solution.findOriginalArray([1, 3, 4, 2, 6, 8]) == [1, 3, 4], 'wrong result'
    assert solution.findOriginalArray([6, 3, 0, 1]) == [], 'wrong result'
    assert solution.findOriginalArray([1]) == [], 'wrong result'


if __name__ == '__main__':
    test_find_original_array()
