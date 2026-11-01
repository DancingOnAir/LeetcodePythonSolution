class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        res = 0
        left = -1
        for right, x in enumerate(nums):
            if minK <= x <= maxK:
                res += right - left
            else:
                left = right
        return res


def test_count_subarrays():
    solution = Solution()
    assert solution.countSubarrays([1, 4, 7, 3], minK=1, maxK=5) == 4, 'wrong result'
    assert solution.countSubarrays([1, 1], minK=1, maxK=1) == 3, 'wrong result'


if __name__ == '__main__':
    test_count_subarrays()
