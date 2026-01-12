from typing import List
from heapq import nsmallest


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return nsmallest(k, points, lambda x: x[0] ** 2 + x[1] ** 2)


def test_k_closest():
    solution = Solution()
    assert solution.kClosest([[1, 3], [-2, 2]], k=1) == [[-2, 2]], 'wrong result'
    assert solution.kClosest([[3, 3], [5, -1], [-2, 4]], k=2) == [[3, 3], [-2, 4]], 'wrong result'


if __name__ == '__main__':
    test_k_closest()
