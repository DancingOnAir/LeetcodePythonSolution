from typing import List


class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        pass


def test_count_pairs():
    solution = Solution()
    assert solution.countPairs([1, 4, 2, 7], 2, 6) == 6, 'wrong result'
    assert solution.countPairs([9, 8, 4, 2, 1], 5, 14) == 8, 'wrong result'


if __name__ == '__main__':
    test_count_pairs()
