from typing import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        s, total = set(nums), nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                break
            total += nums[i]

        while total in s:
            total += 1
        return total


def test_missing_integer():
    solution = Solution()
    assert solution.missingInteger([3, 4, 7, 6, 6, 5, 8, 2, 8, 9, 2, 6]) == 10, 'wrong result'
    assert solution.missingInteger([1, 2, 3, 2, 5]) == 6, 'wrong result'
    assert solution.missingInteger([3, 4, 5, 1, 12, 14, 13]) == 15, 'wrong result'


if __name__ == '__main__':
    test_missing_integer()
