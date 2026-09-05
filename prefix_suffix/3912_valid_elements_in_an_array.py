class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        right_valid = [False] * n
        mx = 0
        for i in range(n - 1, -1, -1):
            right_valid[i] = nums[i] > mx
            mx = max(mx, nums[i])

        res = []
        mx = 0
        for v, x in zip(right_valid, nums):
            if v or x > mx:
                res.append(x)
            mx = max(mx, x)
        return res


def test_find_valid_elements():
    solution = Solution()
    assert solution.findValidElements([1, 2, 4, 2, 3, 2]) == [1, 2, 4, 3, 2], 'wrong result'
    assert solution.findValidElements([5, 5, 5, 5]) == [5, 5], 'wrong result'
    assert solution.findValidElements([1]) == [1], 'wrong result'


if __name__ == '__main__':
    test_find_valid_elements()
