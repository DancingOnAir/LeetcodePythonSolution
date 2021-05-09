class Solution:
    def maxScore(self, s: str) -> int:
        diff = ones = zeros = 0
        for i in range(1, len(s) - 1):
            if s[i] == '1':
                ones += 1
            else:
                zeros += 1
            diff = max(diff, zeros - ones)
        return diff + ones + (s[0] == '0') + (s[-1] == '1')

    # regular method
    def maxScore1(self, s: str) -> int:
        total = sum(map(int, s))

        n = len(s)
        res = cur = 0
        for i, c in enumerate(s[: -1]):
            cur += int(c)
            res = max(res, i + 1 - cur + total - cur)
        return res


def test_max_score():
    solution = Solution()
    assert solution.maxScore('011101') == 5, 'wrong result'
    assert solution.maxScore('00111') == 5, 'wrong result'
    assert solution.maxScore('1111') == 3, 'wrong result'
    assert solution.maxScore('00') == 1, 'wrong result'


if __name__ == '__main__':
    test_max_score()
