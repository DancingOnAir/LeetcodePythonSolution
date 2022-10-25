from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        n = len(nums1)
        diffs = [-abs(nums1[i] - nums2[i]) for i in range(n)]
        if k1 + k2 >= -sum(diffs):
            return 0

        heapify(diffs)
        k = k1 + k2
        while k > 0:
            d = heappop(diffs)
            gap = max(k // n, 1) if diffs else k
            d += gap
            heappush(diffs, d)
            k -= gap
        return sum(d ** 2 for d in diffs)

    # bucket sort
    def minSumSquareDiff2(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        n = len(nums1)
        diffs = [abs(nums1[i] - nums2[i]) for i in range(n)]
        mx = max(diffs)

        buckets = [0] * (mx + 1)
        for diff in diffs:
            buckets[diff] += 1

        k = k1 + k2
        for i in range(len(buckets) - 1, 0, -1):
            if k <= 0:
                break
            if buckets[i] > 0:
                minus = min(buckets[i], k)
                buckets[i] -= minus
                buckets[i - 1] += minus
                k -= minus

        return sum(buckets[i] * i * i for i in range(1, mx + 1))

    # TLE
    def minSumSquareDiff1(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        n = len(nums1)
        diffs = [-abs(nums1[i] - nums2[i]) for i in range(n)]
        k = k1 + k2
        heapify(diffs)

        while k > 0:
            x = heappop(diffs)
            if x == 0:
                return 0
            heappush(diffs, x + 1)
            k -= 1
        return sum(x ** 2 for x in diffs)


def test_min_sum_square_diff():
    solution = Solution()
    assert solution.minSumSquareDiff([1, 2, 3, 4], [2, 10, 20, 19], 0, 0) == 579, 'wrong result'
    assert solution.minSumSquareDiff([1, 4, 10, 12], [5, 8, 6, 9], 1, 1) == 43, 'wrong result'


if __name__ == '__main__':
    test_min_sum_square_diff()
