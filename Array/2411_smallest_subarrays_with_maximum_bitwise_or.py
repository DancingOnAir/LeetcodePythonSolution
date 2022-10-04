from typing import List


class Solution:
    # https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/solutions/2588015/java-c-python-bit-solution-with-explanation/
    # Assume the array has only 0 and 1.
    # Then the question changes:
    # If A[i] = 1, shortest array is [A[i]], length is 1.
    # If A[i] = 0, we need to find the index j of next 1,
    # then j - i + 1 is the length of the shortest subarray.
    # If no next 1, 1 is the length
    #
    # To solve this problem,
    # we can iterate the array reversely
    # and keep the index j of last time we saw 1.
    # res[i] = max(1, last - i + 1)
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        last = [0] * 32
        res = [0] * n
        for i in range(n - 1, -1, -1):
            for j in range(32):
                if nums[i] & (1 << j):
                    last[j] = i
            res[i] = max(1, max(last) - i + 1)
        return res


def test_smallest_subarrays():
    solution = Solution()
    assert solution.smallestSubarrays([1, 0, 2, 1, 3]) == [3, 3, 2, 2, 1], 'wrong result'
    assert solution.smallestSubarrays([1, 2]) == [2, 1], 'wrong result'


if __name__ == '__main__':
    test_smallest_subarrays()
