class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        ones = s.count('1')
        zeros = n - ones
        if ones < 2 or zeros < 1 or n < 3:
            return 0
        if s[0] == s[-1] == '1':
            return min(zeros, ones - 2)
        return min(ones - 1, zeros)


def test_min_flips():
    solution = Solution()
    assert solution.minFlips("1010") == 1, 'wrong result'
    assert solution.minFlips("0110") == 1, 'wrong result'
    assert solution.minFlips("1000") == 0, 'wrong result'


if __name__ == '__main__':
    test_min_flips()
