class Solution:
    def maxRatings(self, units: list[list[int]]) -> int:
        n = len(units[0])
        if n == 1:
            return sum(r[0] for r in units)

        mn = mn2 = float('inf')
        res = 0
        for u in units:
            u.sort()
            res += u[1]
            mn2 = min(mn2, u[1])
            mn = min(mn, u[0])

        res += mn - mn2
        return res


def test_max_rating():
    solution = Solution()
    assert solution.maxRatings([[1,3],[2,2]]) == 4, 'wrong answer'
    assert solution.maxRatings([[1,2,3],[4,5,6]]) == 6, 'wrong answer'
    assert solution.maxRatings([[5,5,5],[1,1,1]]) == 6, 'wrong answer'


if __name__ == '__main__':
    test_max_rating()

