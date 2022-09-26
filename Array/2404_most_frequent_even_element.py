from typing import List
from collections import Counter


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        res = [k for k, v in sorted(Counter(nums).items(), key=lambda x: (-x[1], x[0])) if k % 2 == 0]
        return -1 if not res else res[0]


def test_most_frequent_even():
    solution = Solution()
    assert solution.mostFrequentEven([0, 1, 2, 2, 4, 4, 1]) == 2, 'wrong result'
    assert solution.mostFrequentEven([4, 4, 4, 9, 2, 4]) == 4, 'wrong result'
    assert solution.mostFrequentEven([29, 47, 21, 41, 13, 37, 25, 7]) == -1, 'wrong result'


if __name__ == '__main__':
    test_most_frequent_even()

