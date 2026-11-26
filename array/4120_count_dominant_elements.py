class Solution:
    def countDominantElements(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        res = 0
        for i, x in enumerate(nums):
            if i == 0 and x >= nums[1]:
                res += 1
            elif i == n - 1 and x >= nums[-2]:
                res += 1
            elif 0 < i < n - 1 and x >= (nums[i - 1] + nums[i + 1]) / 2:
                res += 1
        return res


def test_count_dominant_elements():
    solution = Solution()
    assert solution.countDominantElements([1, 10, 2]) == 1, 'wrong result'
    assert solution.countDominantElements([6, 4, 2]) == 2, 'wrong result'
    assert solution.countDominantElements([7]) == 1, 'wrong result'


if __name__ == '__main__':
    test_count_dominant_elements()
