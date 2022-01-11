from typing import List
from collections import Counter


class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        def check(nums, k):
            res = list()
            cnt = Counter(nums)
            for num in nums:
                if cnt[num] == 0:
                    continue
                if cnt[num + k] == 0:
                    return False, []

                cnt[num] -= 1
                cnt[num + k] -= 1
                res.append(num + k // 2)

            return True, res

        nums = sorted(nums)
        for i in range(1, len(nums)):
            diff = nums[i] - nums[0]
            if diff != 0 and diff % 2 == 0:
                a, b = check(nums, diff)

                if a:
                    return b


def test_recover_array():
    solution = Solution()

    assert solution.recoverArray([2, 10, 6, 4, 8, 12]) == [3, 7, 11], 'wrong result'
    assert solution.recoverArray([1, 1, 3, 3]) == [2, 2], 'wrong result'
    assert solution.recoverArray([5, 435]) == [220], 'wrong result'


if __name__ == '__main__':
    test_recover_array()
