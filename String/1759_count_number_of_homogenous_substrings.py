class Solution:
    def countHomogenous(self, s: str) -> int:
        n = 1
        res = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                n += 1
            else:
                res += (1 + n) * n // 2
                n = 1

        res += (1 + n) * n // 2
        return res % (10 ** 9 + 7)


def test_count_homogenous():
    solution = Solution()
    assert solution.countHomogenous('abbcccaa') == 13, 'wrong result'
    assert solution.countHomogenous('xy') == 2, 'wrong result'
    assert solution.countHomogenous('zzzzz') == 15, 'wrong result'


if __name__ == '__main__':
    test_count_homogenous()
