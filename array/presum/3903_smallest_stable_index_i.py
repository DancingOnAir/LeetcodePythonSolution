class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        mn = [float('inf')] * n
        mn[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            mn[i] = min(mn[i + 1], nums[i])

        mx = nums[0]
        for i, x in enumerate(nums):
            if i > 0:
                mx = max(mx, x)
            if mx - mn[i] <= k:
                return i
        return -1


def test_first_stable_index():
    solution = Solution()
    assert solution.firstStableIndex([5,0,1,4], 3) == 3, 'wrong result'
    assert solution.firstStableIndex([3,2,1], 1) == -1, 'wrong result'
    assert solution.firstStableIndex([0], 0) == 0, 'wrong result'


if __name__ == '__main__':
    test_first_stable_index()
