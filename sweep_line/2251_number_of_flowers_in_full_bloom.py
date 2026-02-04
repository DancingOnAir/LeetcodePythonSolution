from typing import List
from bisect import bisect_right, bisect_left
from collections import defaultdict


class Solution:
    # binary search
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        start = sorted(s for s, e in flowers)
        end = sorted(e for s, e in flowers)
        return [bisect_right(start, p) - bisect_left(end, p) for p in persons]

    # sweep line
    def fullBloomFlowers1(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        endpoints = defaultdict(int)
        for i, j in flowers:
            endpoints[i] += 1
            endpoints[j + 1] += -1

        bloom = list()
        cur = 0
        sorted_endpoints = sorted(endpoints)
        for i in sorted_endpoints:
            cur += endpoints[i]
            bloom.append(cur)

        return [bloom[bisect_right(sorted_endpoints, p) - 1] for p in persons]


def test_full_bloom_flowers():
    solution = Solution()
    assert solution.fullBloomFlowers([[19, 37], [19, 38], [19, 35]], [6, 7, 21, 1, 13, 37, 5, 37, 46, 43]) == [0, 0, 3, 0, 0, 2, 0, 2, 0, 0], 'wrong result'
    assert solution.fullBloomFlowers([[1, 6], [3, 7], [9, 12], [4, 13]], [2, 3, 7, 11]) == [1, 2, 2, 2], 'wrong result'
    assert solution.fullBloomFlowers([[1, 10], [3, 3]], [3, 3, 2]) == [2, 2, 1], 'wrong result'


if __name__ == '__main__':
    test_full_bloom_flowers()
