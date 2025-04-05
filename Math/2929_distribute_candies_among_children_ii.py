class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def cal(x):
            return 0 if x < 0 else x * (x - 1) // 2
        return cal(n + 2) - cal(n + 2 - (limit + 1)) * 3 + cal(n + 2 - 2 * (limit + 1)) * 3 - cal(n + 2 - 3 * (limit + 1))


def test_distribute_candies():
    solution = Solution()
    assert solution.distributeCandies(5, 2) == 3, 'wrong result'
    assert solution.distributeCandies(3, 3) == 10, 'wrong result'


if __name__ == '__main__':
    test_distribute_candies()
