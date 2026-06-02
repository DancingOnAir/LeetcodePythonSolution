class Solution:
    def minOperations(self, nums: list[int]) -> int:
        return 0


def test_min_operations():
    solution = Solution()
    assert solution.minOperations([1, 2, 3, 4]) == 3, 'wrong result'
    assert solution.minOperations([5, 6, 7, 8]) == 0, 'wrong result'
    assert solution.minOperations([4, 4]) == 1, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
