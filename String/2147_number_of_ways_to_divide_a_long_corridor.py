class Solution:
    def numberOfWays(self, corridor: str) -> int:
        m = list()
        for i, ch in enumerate(corridor):
            if ch == 'S':
                m.append(i)

        n = len(m)
        if n == 0 or (n & 1):
            return 0

        res = 1
        for i in range(1, n - 2, 2):
            res *= (m[i + 1] - m[i])

        return res % (10 ** 9 + 7)


def test_number_of_ways():
    solution = Solution()
    assert solution.numberOfWays('SSPSSPSSSPPSPSPPS') == 8, 'wrong reuslt'
    assert solution.numberOfWays('SSPPSPS') == 3, 'wrong reuslt'
    assert solution.numberOfWays('PPSPSP') == 1, 'wrong reuslt'
    assert solution.numberOfWays('S') == 0, 'wrong reuslt'


if __name__ == '__main__':
    test_number_of_ways()
