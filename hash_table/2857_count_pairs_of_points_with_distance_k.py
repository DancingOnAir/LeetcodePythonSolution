from typing import List
from collections import Counter


class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        res = 0
        cnt = Counter()
        for x, y in coordinates:
            for i in range(k + 1):
                res += cnt[(x ^ i, y ^ (k - i))]
            cnt[(x, y)] += 1
        return res


def test_count_pairs():
    solution = Solution()
    assert solution.countPairs([[1, 2], [4, 2], [1, 3], [5, 2]], k=5) == 2, 'wrong result'
    assert solution.countPairs([[1, 3], [1, 3], [1, 3], [1, 3], [1, 3]], k=0) == 10, 'wrong result'


if __name__ == '__main__':
    test_count_pairs()
