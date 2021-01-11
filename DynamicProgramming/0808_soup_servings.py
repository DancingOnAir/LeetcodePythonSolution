from math import ceil


class Solution:
    def soupServings(self, N: int) -> float:
        memo = dict()

        if N > 4800:
            return 1.0

        def dp(x, y):
            if (x, y) in memo:
                return memo[(x, y)]
            if x <= 0 and y <= 0:
                return 0.5
            if x <= 0:
                return 1.0
            if y <= 0:
                return 0.0
            memo[(x, y)] = 0.25 * (dp(x-4, y) + dp(x-3, y-1) + dp(x-2, y-2) + dp(x-1, y-3))
            return memo[(x, y)]
        N = ceil(N / 25.0)
        return dp(N, N)

    def soupServings1(self, N: int) -> float:
        d, m = divmod(N, 25)
        N = d + (m > 0)
        # every time for A = 0.25 * (4 + 3 + 2 + 1) = 2.5; for B = 0.25 * (1 + 2 + 3) = 1.5
        # A decreases 1 more than B each time.
        if N >= 500:
            return 1

        memo = dict()

        def dp(x, y):
            if (x, y) not in memo:
                if x <= 0 or y <= 0:
                    ans = 0.5 if x <= 0 and y <= 0 else 1.0 if x <= 0 else 0.0
                else:
                    ans = 0.25 * (dp(x - 4, y) + dp(x - 3, y - 1) + dp(x - 2, y - 2) + dp(x - 1, y - 3))
                memo[x, y] = ans

            return memo[x, y]
        return dp(N, N)


def test_soup_servings():
    solution = Solution()

    assert solution.soupServings(50) == 0.625, 'wrong result'


if __name__ == '__main__':
    test_soup_servings()
