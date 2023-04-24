from typing import List
from heapq import heappush, heappop


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res = total = 0
        h = list()
        for a, b in sorted(list(zip(nums1, nums2)), key=lambda ab: -ab[1]):
            total += a
            heappush(h, a)
            if len(h) > k:
                total -= heappop(h)
            if len(h) == k:
                res = max(res, b * total)
        return res


def test_max_score():
    solution = Solution()
    assert solution.maxScore([1, 3, 3, 2], [2, 1, 3, 4], 3) == 12, 'wrong result'
    assert solution.maxScore([4, 2, 3, 1, 1], [7, 5, 10, 9, 6], 1) == 30, 'wrong result'


if __name__ == '__main__':
    test_max_score()
