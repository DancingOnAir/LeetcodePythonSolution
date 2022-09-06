from typing import List
from itertools import accumulate
from collections import Counter


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        pre_sum = [0] + list(accumulate(travel))
        distance = dict()
        freq = Counter()
        for i, g in enumerate(garbage):
            cur = Counter(g)
            freq += cur
            for k in cur:
                distance[k] = i

        res = 0
        for k, v in freq.items():
            res += pre_sum[distance[k]] + v
        return res


def test_garbage_collection():
    solution = Solution()
    assert solution.garbageCollection(["G", "P", "GP", "GG"], [2, 4, 3]) == 21, 'wrong result'
    assert solution.garbageCollection(["MMM", "PGM", "GP"], [3, 10]) == 37, 'wrong result'


if __name__ == '__main__':
    test_garbage_collection()
