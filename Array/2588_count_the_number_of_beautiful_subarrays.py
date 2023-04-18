from typing import List


class Solution:
    # brute force, but TLE
    def beautifulSubarrays(self, nums: List[int]) -> int:
        pre_sum = [0]
        for x in nums:
            pre_sum.append(pre_sum[-1] ^ x)

        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if (pre_sum[j + 1] ^ pre_sum[i]) == 0:
                    res += 1
        return res


def test_beautiful_subarrays():
    solution = Solution()
    assert solution.beautifulSubarrays([4, 3, 1, 2, 4]) == 2, 'wrong result'
    assert solution.beautifulSubarrays([1, 10, 4]) == 0, 'wrong result'


if __name__ == '__main__':
    test_beautiful_subarrays()
