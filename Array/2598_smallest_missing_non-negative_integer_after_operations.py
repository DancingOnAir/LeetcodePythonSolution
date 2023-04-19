from typing import List
from collections import Counter


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        c = Counter(x % value for x in nums)
        res = 0
        while c[res % value] > 0:
            c[res % value] -= 1
            res += 1

        return res


def test_find_smallest_integer():
    solution = Solution()
    assert solution.findSmallestInteger([1, -10, 7, 13, 6, 8], 5) == 4, 'wrong result'
    assert solution.findSmallestInteger([1, -10, 7, 13, 6, 8], 7) == 2, 'wrong result'


if __name__ == '__main__':
    test_find_smallest_integer()
