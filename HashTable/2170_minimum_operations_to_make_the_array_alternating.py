from typing import List
from collections import defaultdict


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        even = [0] * 100001
        odd = [0] * 100001

        a = b = c = d = 0
        for i, x in enumerate(nums):
            if i & 1:
                even[x] += 1
                if a == 0 or even[x] > even[a]:
                    a, b = x, a
                elif x != a and (b == 0 or even[x] > even[b]):
                    b = x
            else:
                odd[x] += 1
                if c == 0 or odd[x] > odd[c]:
                    c, d = x, c
                elif x != c and (d == 0 or odd[x] > odd[d]):
                    d = x
        if a != c:
            return n - even[a] - odd[c]
        return n - max(even[a] + odd[d], even[b] + odd[c])

    def minimumOperations1(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        even_cnt = defaultdict(int)
        odd_cnt = defaultdict(int)
        for i, x in enumerate(nums):
            if i & 1:
                odd_cnt[x] += 1
            else:
                even_cnt[x] += 1

        res = n
        for k1, v1 in sorted([(k, v) for k, v in even_cnt.items()], key=lambda x: -x[1])[:2]:
            for k2, v2 in sorted([(k, v) for k, v in odd_cnt.items()], key=lambda x: -x[1])[:2]:
                if k1 == k2:
                    res = min(res, n - max(v1, v2))
                else:
                    res = min(res, n - v1 - v2)
        return res


def test_minimum_operations():
    solution = Solution()
    assert solution.minimumOperations([3, 1, 3, 2, 4, 3]) == 3, 'wrong result'
    assert solution.minimumOperations([1, 2, 2, 2, 2]) == 2, 'wrong result'


if __name__ == '__main__':
    test_minimum_operations()
