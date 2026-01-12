class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def comb(x):
            if x < 0:
                return 0
            return x * (x - 1) // 2
        return comb(n + 2) - 3 * comb(n - limit + 1) + 3 * comb(n - 2 * limit) - comb(n - 3 * limit - 1)


def test_distribute_candies():
    solution = Solution()
    assert solution.distributeCandies(5, 2) == 3, 'wrong result'
    assert solution.distributeCandies(3, 3) == 10, 'wrong result'


if __name__ == '__main__':
    test_distribute_candies()
