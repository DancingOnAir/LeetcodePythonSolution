from typing import List
from itertools import permutations


class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        return max(int(''.join(map(lambda x: bin(x)[2:], a)), 2) for a in permutations(nums))


def test_max_good_number():
    solution = Solution()
    # 1, 1011, 101 -> 1 101 1011 or 1 1011 101
    assert solution.maxGoodNumber([1, 11, 5]) == 221, 'wrong result'
    assert solution.maxGoodNumber([1, 2, 3]) == 30, 'wrong result'
    assert solution.maxGoodNumber([2, 8, 16]) == 1296, 'wrong result'


if __name__ == '__main__':
    test_max_good_number()
