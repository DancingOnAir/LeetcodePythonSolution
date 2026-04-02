class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        res = tot = l = 0
        for r, x in enumerate(nums):
            tot += 1 if x else -1
            if l <= r and tot == 0:
                res = max(res, r - l + 1)
                tot -= 1 if nums[l] else -1
                l += 1

        return res


def test_find_max_length():
    solution = Solution()
    assert solution.findMaxLength([0, 1]) == 2, 'wrong result'
    assert solution.findMaxLength([0, 1, 0]) == 2, 'wrong result'
    assert solution.findMaxLength([0, 1, 1, 1, 1, 1, 0, 0, 0]) == 6, 'wrong result'


if __name__ == '__main__':
    test_find_max_length()
