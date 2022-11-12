from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        j, res = 0, 1

        for i in range(len(nums)):
            if nums[i] - nums[j] > k:
                j = i
                res += 1
        return res

    def partitionArray1(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 1
        mx = mn = nums[0]
        for x in nums:
            mx = max(mx, x)
            mn = min(mn, x)
            if mx - mn > k:
                res += 1
                mx = mn = x
        return res


def test_partition_array():
    solution = Solution()
    assert solution.partitionArray([16, 8, 17, 0, 3, 17, 8, 20], 10) == 2, 'wrong result'
    assert solution.partitionArray([3, 6, 1, 2, 5], 2) == 2, 'wrong result'
    assert solution.partitionArray([1, 2, 3], 1) == 2, 'wrong result'
    assert solution.partitionArray([2, 2, 4, 5], 0) == 3, 'wrong result'


if __name__ == '__main__':
    test_partition_array()
