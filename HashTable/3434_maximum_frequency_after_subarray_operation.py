from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        pass


def test_max_frequency():
    solution = Solution()
    assert solution.maxFrequency([1, 2, 3, 4, 5, 6], 1) == 2, 'wrong result'
    assert solution.maxFrequency([10, 2, 3, 4, 5, 5, 4, 3, 2, 2], 10) == 4, 'wrong result'


if __name__ == '__main__':
    test_max_frequency()
