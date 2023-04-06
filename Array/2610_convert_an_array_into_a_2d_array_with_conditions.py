from typing import List
from collections import Counter


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = list()
        n = len(nums)
        c = Counter(nums)
        while n:
            cur = list()
            for k, v in c.items():
                if v > 0:
                    cur.append(k)
                    c[k] -= 1
                    n -= 1
            res.append(cur)
        return res


def test_find_matrix():
    solution = Solution()
    assert solution.findMatrix([1, 3, 4, 1, 2, 3, 1]) == [[1, 3, 4, 2], [1, 3], [1]], 'wrong result'
    assert solution.findMatrix([1, 2, 3, 4]) == [[4, 3, 2, 1]], 'wrong result'


if __name__ == '__main__':
    test_find_matrix()
