class Solution:
    def maxSubarray(self, nums: list[int]) -> int:
        mx = max(nums)
        cnt_sum = [0] * (mx * 2 + 1)
        cnt_diff = [0] * (mx + 1)
        res = left = 0
        for right, x in enumerate(nums):
            while cnt_sum[x] > 0 or cnt_diff[x] > 0:
                y = nums[left]
                left += 1
                for z in nums[left: right]:
                    cnt_sum[y + z] -= 1
                    cnt_diff[abs(y - z)] -= 1

            for y in nums[left: right]:
                cnt_sum[x + y] += 1
                cnt_diff[abs(x - y)] += 1
            res = max(res, right - left + 1)

        return res


def test_max_subarray():
    solution = Solution()
    assert solution.maxSubarray([2, 3, 5, 3, 2, 1]) == 3, 'wrong result'
    assert solution.maxSubarray([3, 4, 5, 6]) == 4, 'wrong result'


if __name__ == '__main__':
    test_max_subarray()

