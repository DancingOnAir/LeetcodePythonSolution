from typing import List


class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        if nums[0] != 0:
            return 0
        # 二进制全部为1
        res = -1
        for i, x in enumerate(nums):
            if i != x:
                res &= x
        return max(0, res)


def test_sort_permutation():
    solution = Solution()
    assert solution.sortPermutation([0, 3, 2, 1]) == 1, 'wrong result'
    assert solution.sortPermutation([0, 1, 3, 2]) == 2, 'wrong result'
    assert solution.sortPermutation([3, 2, 1, 0]) == 0, 'wrong result'


if __name__ == '__main__':
    test_sort_permutation()
