from typing import List


class Solution:
    # pre-sum + binary search
    def countSubarrays(self, nums: List[int], k: int) -> int:
        pre_sum = [0]
        for x in nums:
            pre_sum.append(pre_sum[-1] + x)

        res = 0
        for i in range(1, len(nums) + 1):
            l, r = i, len(nums)
            cur = -1
            while l <= r:
                mid = l + (r - l) // 2
                total = (pre_sum[mid] - pre_sum[i - 1]) * (mid - i + 1)
                if total >= k:
                    r = mid - 1
                else:
                    l = mid + 1
                    cur = mid
            if cur != -1:
                res += cur - i + 1
        return res

    # sliding window
    def countSubarrays1(self, nums: List[int], k: int) -> int:
        res = i = total = 0
        for j, v in enumerate(nums):
            total += v
            while total * (j - i + 1) >= k:
                total -= nums[i]
                i += 1
            res += j - i + 1

        return res


def test_count_subarrays():
    solution = Solution()
    assert solution.countSubarrays([2, 1, 4, 3, 5], 10) == 6, 'wrong result'
    assert solution.countSubarrays([1, 1, 1], 5) == 5, 'wrong result'


if __name__ == '__main__':
    test_count_subarrays()
