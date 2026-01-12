from typing import List


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)

        if sum(nums) == ((n * (n + 1) // 2) + n) and len(nums) == n + 1 and len(set(nums)) == n:
            return True
        return False

    def isGood1(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False

        nums.sort()
        cur = 1
        for i in range(n - 1):
            if cur != nums[i]:
                return False
            cur += 1

        return cur - 1 == nums[-1]


def test_is_good():
    solution = Solution()
    assert not solution.isGood([9, 9]), 'wrong result'
    assert not solution.isGood([2, 1, 3]), 'wrong result'
    assert solution.isGood([1, 3, 3, 2]), 'wrong result'
    assert solution.isGood([1, 1]), 'wrong result'
    assert not solution.isGood([3, 4, 4, 1, 2, 1]), 'wrong result'


if __name__ == '__main__':
    test_is_good()
