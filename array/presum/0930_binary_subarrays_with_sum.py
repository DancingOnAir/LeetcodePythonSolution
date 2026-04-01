class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        res = l1 = l2 = tot1 = tot2 = 0
        for r, x in enumerate(nums):
            tot1 += x
            tot2 += x
            while l1 <= r and tot1 >= goal:
                tot1 -= nums[l1]
                l1 += 1
            while l2 <= r and tot2 >= goal + 1:
                tot2 -= nums[l2]
                l2 += 1
            res += (l1 - l2)
        return res


def test_num_subarrays_with_sum():
    solution = Solution()
    assert solution.numSubarraysWithSum([1, 0, 1, 0, 1], 2) == 4, 'wrong result'
    assert solution.numSubarraysWithSum([0, 0, 0, 0, 0], 0) == 15, 'wrong result'


if __name__ == '__main__':
    test_num_subarrays_with_sum()
