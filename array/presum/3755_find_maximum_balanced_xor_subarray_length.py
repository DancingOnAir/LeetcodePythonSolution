from typing import List


class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        acc = 0
        balance = 0
        m = {(0, 0): -1}
        res = 0
        for i, x in enumerate(nums):
            acc ^= x
            balance += 1 if x & 1 else -1
            k = (acc, balance)
            if k in m:
                res = max(res, i - m[k])
            else:
                m[k] = i
        return res


def test_max_balanced_subarray():
    solution = Solution()
    assert solution.maxBalancedSubarray([3, 1, 3, 2, 0]) == 4, "test1"
    assert solution.maxBalancedSubarray([3, 2, 8, 5, 4, 14, 9, 15]) == 8, "test2"
    assert solution.maxBalancedSubarray([0]) == 0, "test3"


if __name__ == '__main__':
    test_max_balanced_subarray()
