from typing import List
from heapq import heappop, heappush


class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        hp = []
        res = []
        for x, y in queries:
            heappush(hp, -abs(x) - abs(y))
            if len(hp) > k:
                heappop(hp)

            if len(hp) == k:
                res.append(-hp[0])
            else:
                res.append(-1)
        return res


def test_results_array():
    solution = Solution()
    assert solution.resultsArray([[1, 2], [3, 4], [2, 3], [-3, 0]], 2) == [-1, 7, 5, 3], 'wrong result'
    assert solution.resultsArray([[5, 5], [4, 4], [3, 3]], 1) == [10, 8, 6], 'wrong result'


if __name__ == '__main__':
    test_results_array()
