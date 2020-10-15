from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
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


if __name__ == '__main__':
    test_longest_subarray()
