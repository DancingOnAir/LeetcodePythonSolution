class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suf_min = [float('inf')] * n
        suf_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suf_min[i] = min(suf_min[i + 1], nums[i])

        pre_max = 0
        for i, x in enumerate(nums):
            pre_max = max(pre_max, x)
            if pre_max - suf_min[i] <= k:
                return i
        return -1


def test_first_stable_index():
    solution = Solution()
    assert solution.firstStableIndex([5, 0, 1, 4], 3) == 3, 'wrong result'
    assert solution.firstStableIndex([3, 2, 1], 1) == -1, 'wrong result'
    assert solution.firstStableIndex([0], 0) == 0, 'wrong result'


if __name__ == '__main__':
    test_first_stable_index()
