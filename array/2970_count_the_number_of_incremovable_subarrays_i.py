from typing import List


class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i, n):
                pre = -1
                flag = True
                for k in range(n):
                    if i <= k <= j:
                        continue
                    else:
                        flag &= (pre < nums[k])
                        pre = nums[k]
                res += int(flag)
        return res


def test_incremovable_subarray_count():
    solution = Solution()
    assert solution.incremovableSubarrayCount([1, 2, 3, 4]) == 10, 'wrong result'
    assert solution.incremovableSubarrayCount([6, 5, 7, 8]) == 7, 'wrong result'
    assert solution.incremovableSubarrayCount([8, 7, 6, 6]) == 3, 'wrong result'


if __name__ == '__main__':
    test_incremovable_subarray_count()
