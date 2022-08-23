from typing import List


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        res = 0
        pre = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            k = (nums[i] - 1) // pre
            res += k
            pre = nums[i] // (k + 1)

        return res


def test_minimum_replacement():
    solution = Solution()
    assert solution.minimumReplacement([2, 10, 20, 19, 1]) == 47, 'wrong result'
    assert solution.minimumReplacement([3, 9, 3]) == 2, 'wrong result'
    assert solution.minimumReplacement([1, 2, 3, 4, 5]) == 0, 'wrong result'


if __name__ == '__main__':
    test_minimum_replacement()
