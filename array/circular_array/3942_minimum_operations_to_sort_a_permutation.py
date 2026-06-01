class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        asc, dsc = 1, 1
        for i in range(1, n):
            asc += nums[i] == (nums[i - 1] + 1) % n
            dsc += nums[i - 1] == (nums[i] + 1) % n

        if asc == n and not nums[0]:
            return 0
        if asc == n:
            return min(n - nums[0], nums[0] + 2)
        if dsc == n:
            return min(n - nums[-1], nums[-1]) + 1
        return -1


def test_min_operations():
    solution = Solution()
    assert solution.minOperations([0, 2, 1]) == 2, 'wrong result'
    assert solution.minOperations([1, 0, 2]) == 2, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
