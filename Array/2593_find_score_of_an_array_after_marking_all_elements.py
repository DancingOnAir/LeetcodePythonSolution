from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        nums = sorted([[v, i] for i, v in enumerate(nums)], reverse=True)
        res, n = 0, len(nums)
        seen = set()
        while nums:
            cur = nums.pop()
            if cur[1] not in seen:
                res += cur[0]
                seen.add(cur[1])
                if cur[1] < n - 1:
                    seen.add(cur[1] + 1)
                if cur[1] > 0:
                    seen.add(cur[1] - 1)
        return res


def test_find_score():
    solution = Solution()
    assert solution.findScore(
        [10, 44, 10, 8, 48, 30, 17, 38, 41, 27, 16, 33, 45, 45, 34, 30, 22, 3, 42, 42]) == 212, 'wrong result'
    assert solution.findScore([2, 1, 3, 4, 5, 2]) == 7, 'wrong result'
    assert solution.findScore([2, 3, 5, 1, 3, 2]) == 5, 'wrong result'


if __name__ == '__main__':
    test_find_score()
