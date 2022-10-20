from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums = set(nums)
        return max([x for x in nums if -x in nums], default=-1)

    def findMaxK1(self, nums: List[int]) -> int:
        return max([x for x in nums if -x in set(nums)], default=-1)


def test_find_max_k():
    solution = Solution()
    assert solution.findMaxK([-1, 2, -3, 3]) == 3, 'wrong result'
    assert solution.findMaxK([-1, 10, 6, 7, -7, 1]) == 7, 'wrong result'
    assert solution.findMaxK([-10, 8, 6, 7, -2, -3]) == -1, 'wrong result'


if __name__ == '__main__':
    test_find_max_k()
