from typing import List
from collections import Counter


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        mx = max(cnt.values())
        return sum(v for _, v in cnt.items() if v == mx)


def test_max_frequency_elements():
    solution = Solution()
    assert solution.maxFrequencyElements([1, 2, 2, 3, 1, 4]) == 4, 'wrong result'
    assert solution.maxFrequencyElements([1, 2, 3, 4, 5]) == 5, 'wrong result'


if __name__ == '__main__':
    test_max_frequency_elements()
