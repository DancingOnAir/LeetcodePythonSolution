from typing import List


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        return 0 if sum(nums) & 1 else len(nums) - 1


def test_count_partitions():
    solution = Solution()
    assert solution.countPartitions([10, 10, 3, 7, 6]) == 4, 'wrong result'
    assert solution.countPartitions([1, 2, 2]) == 0, 'wrong result'
    assert solution.countPartitions([2, 4, 6, 8]) == 3, 'wrong result'


if __name__ == '__main__':
    test_count_partitions()
