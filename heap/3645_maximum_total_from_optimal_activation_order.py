from typing import List
from collections import defaultdict


class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        cnt = defaultdict(list)
        for l, v in zip(limit, value):
            cnt[l].append(v)

        res = 0
        for l, arr in cnt.items():
            arr.sort()
            res += sum(arr[-l:])
        return res


def test_max_total():
    solution = Solution()
    assert solution.maxTotal([3, 5, 8], limit=[2, 1, 3]) == 16, 'wrong result'
    assert solution.maxTotal([4, 2, 6], limit=[1, 1, 1]) == 6, 'wrong result'
    assert solution.maxTotal([4, 1, 5, 2], limit=[3, 3, 2, 3]) == 12, 'wrong result'


if __name__ == '__main__':
    test_max_total()
