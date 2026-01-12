from typing import List


class Solution:
    # sliding window
    def longestSubarray(self, nums: List[int]) -> int:
        left, count, res = 0, 0, 0
        for right in range(len(nums)):
            if not nums[right]:
                count += 1

            while left < right and count > 1:
                if not nums[left]:
                    count -= 1
                left += 1
            res = max(res, right - left)
        return res

    # prefix sum & suffix sum
    def longestSubarray2(self, nums: List[int]) -> int:
        n = len(nums)
        pre, suf = [nums[0]] + [0] * (n - 1), [0] * (n - 1) + [nums[-1]]

        for i in range(1, n):
            if nums[i]:
                pre[i] = pre[i - 1] + 1

        for i in range(n - 1)[::-1]:
            if nums[i]:
                suf[i] = suf[i + 1] + 1

        res = 0
        for i in range(n):
            pre_sum = pre[i - 1] if i else 0
            suf_sum = suf[i + 1] if i != n - 1 else 0
            res = max(res, pre_sum + suf_sum)

        return res

    # optimized prefix & suffix sum
    def longestSubarray1(self, nums: List[int]) -> int:
        # a is the len of subarray which contains a one, b is the length of subarray which only contains ones
        a, b = 0, 0
        res = 0
        for i, val in enumerate(nums):
            if not val:
                a = b
                b = 0
            else:
                a += 1
                b += 1
                res = max(res, a)

        if res == len(nums):
            res -= 1
        return res


def test_longest_subarray():
    solution = Solution()

    nums1 = [1, 1, 0, 1]
    print(solution.longestSubarray(nums1))

    nums2 = [0, 1, 1, 1, 0, 1, 1, 0, 1]
    print(solution.longestSubarray(nums2))

    nums3 = [1, 1, 1]
    print(solution.longestSubarray(nums3))

    nums4 = [1, 1, 0, 0, 1, 1, 1, 0, 1]
    print(solution.longestSubarray(nums4))

    nums5 = [0, 0, 0]
    print(solution.longestSubarray(nums5))

    nums6 = [0, 1, 1, 1, 0, 1, 1]
    print(solution.longestSubarray(nums6))


if __name__ == '__main__':
    test_longest_subarray()
