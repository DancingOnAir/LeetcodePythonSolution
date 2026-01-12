from typing import List


class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        m = len(pattern)
        pattern.append(2)
        pattern.extend([(y > x) - (y < x) for x, y in zip(nums, nums[1:])])

        n = len(pattern)
        z = [0] * n
        res, l, r = 0, 0, 0
        for i in range(1, n):
            if i <= r:
                z[i] = min(z[i - l], r - i + 1)

            while z[i] + i < n and pattern[z[i]] == pattern[z[i] + i]:
                l, r = i, z[i] + i
                z[i] += 1

            if z[i] >= m:
                res += 1

        return res


def test_count_matching_subarrays():
    solution = Solution()
    assert solution.countMatchingSubarrays([1, 2, 3, 4, 5, 6], [1, 1]) == 4, 'wrong result'
    assert solution.countMatchingSubarrays([1, 4, 4, 1, 3, 5, 5, 3], [1, 0, -1]) == 2, 'wrong result'


if __name__ == '__main__':
    test_count_matching_subarrays()
