from typing import List
from collections import defaultdict


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for i, val in enumerate(nums):
            freq[i - val] += 1
        good = sum(v * (v - 1) // 2 for v in freq.values() if v > 1)
        return len(nums) * (len(nums) - 1) // 2 - good


def test_count_bad_pairs():
    solution = Solution()
    assert solution.countBadPairs([4, 1, 3, 3]) == 5, 'wrong result'
    assert solution.countBadPairs([1, 2, 3, 4, 5]) == 0, 'wrong result'


if __name__ == '__main__':
    test_count_bad_pairs()

