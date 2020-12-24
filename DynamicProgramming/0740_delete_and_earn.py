from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        values = [0] * 10001
        for num in nums:
            values[num] += num

        take, skip = 0, 0
        for i in range(10001):
            take_i = skip + values[i]
            skip_i = max(take, skip)

            take = take_i
            skip = skip_i

        return max(take, skip)


def test_delete_and_earn():
    solution = Solution()

    # nums1 = [3, 4, 2]
    # assert solution.deleteAndEarn(nums1) == 6, 'wrong result'
    #
    # nums2 = [2, 2, 3, 3, 3, 4]
    # assert solution.deleteAndEarn(nums2) == 9, 'wrong result'

    nums3 = [8, 7, 3, 8, 1, 4, 10, 10, 10, 2]
    assert solution.deleteAndEarn(nums3) == 52, 'wrong result'


if __name__ == '__main__':
    test_delete_and_earn()
