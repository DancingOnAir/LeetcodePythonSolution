from typing import List
from functools import cmp_to_key


class Solution:
    def kthLargestNumber1(self, nums: List[str], k: int) -> str:
        nums = sorted(list(map(int, nums)))
        return str(nums[-k])


def test_kth_largest_number():
    solution = Solution()
    assert solution.kthLargestNumber(["3", "6", "7", "10"], 4) == "3", 'wrong result'
    assert solution.kthLargestNumber(["2", "21", "12", "1"], 3) == "2", 'wrong result'
    assert solution.kthLargestNumber(["0", "0"], 2) == "0", 'wrong result'


if __name__ == '__main__':
    test_kth_largest_number()
