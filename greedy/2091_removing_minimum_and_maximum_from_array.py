class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)
        mn = float('inf')
        mx = float('-inf')
        mn_id = mx_id = 0
        for i, x in enumerate(nums):
            if mn > x:
                mn = x
                mn_id = i
            if mx < x:
                mx = x
                mx_id = i

        if mn_id > mx_id:
            mn_id, mx_id = mx_id, mn_id
        return min(mx_id + 1, n - mn_id, mn_id + 1 + n - mx_id)


def test_minimum_deletions():
    solution = Solution()
    assert solution.minimumDeletions([2, 10, 7, 5, 4, 1, 8, 6]) == 5, 'wrong result'
    assert solution.minimumDeletions([0, -4, 19, 1, 8, -2, -3, 5]) == 3, 'wrong result'
    assert solution.minimumDeletions([101]) == 1, 'wrong result'


if __name__ == '__main__':
    test_minimum_deletions()
