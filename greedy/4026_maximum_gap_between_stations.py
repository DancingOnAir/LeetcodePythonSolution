class Solution:
    def maximumGap(self, skill: str, station: str) -> int:
        m, n = len(station), len(skill)
        if n == 1:
            return 0

        earliest = [0] * n
        latest = [0] * n
        j = 0
        for i, c in enumerate(station):
            if c == skill[j]:
                earliest[j] = i
                j += 1
            if j == n:
                break

        j = n - 1
        for i in range(m - 1, -1, -1):
            if station[i] == skill[j]:
                latest[j] = i
                j -= 1
            if j == -1:
                break

        return max(latest[i + 1] - earliest[i] for i in range(n - 1))


def test_maximum_gap():
    solution = Solution()
    assert solution.maximumGap("aa", station = "aaaa") == 3, 'wrong result'
    assert solution.maximumGap("xyz", station = "xyzz") == 2, 'wrong result'
    assert solution.maximumGap("cbc", station = "cbcdbc") == 4, 'wrong result'


if __name__ == '__main__':
    test_maximum_gap()
