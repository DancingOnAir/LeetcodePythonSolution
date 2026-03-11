from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        seen = set()
        res = 0
        for i in range(n):
            diff = 0
            for j in range(i, n):
                x = nums[j]
                if x not in seen:
                    diff += 1 - (x & 1) * 2
                    seen.add(x)
                if diff == 0:
                    res = max(res, j - i + 1)
            seen.clear()
        return res


def test_longest_balanced():
    solution = Solution()
    assert solution.longestBalanced([2, 5, 4, 3]) == 4, 'wrong result'
    assert solution.longestBalanced([3, 2, 2, 5, 4]) == 5, 'wrong result'
    assert solution.longestBalanced([1, 2, 3, 2]) == 3, 'wrong result'


if __name__ == '__main__':
    test_longest_balanced()
