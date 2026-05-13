class Solution:
    def dominantIndices(self, nums: list[int]) -> int:
        n = len(nums)
        res, tot = 0, nums[-1]
        for i in range(n - 2, -1, -1):
            if nums[i] > tot / (n - 1 - i):
                res += 1
            tot += nums[i]
        return res


def test_dominant_indices():
    solution = Solution()
    assert solution.dominantIndices([5, 4, 3]) == 2, 'wrong result'
    assert solution.dominantIndices([4, 1, 2]) == 1, 'wrong result'


if __name__ == '__main__':
    test_dominant_indices()
