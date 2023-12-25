class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        res, s = 0, str(num)
        for i in range(len(s) - k + 1):
            x = int(s[i: i+k])
            if x != 0 and num % x == 0:
                res += 1
        return res


def test_divisor_substrings():
    solution = Solution()
    assert solution.divisorSubstrings(240, 2) == 2, 'wrong result'
    assert solution.divisorSubstrings(430043, 2) == 2, 'wrong result'


if __name__ == '__main__':
    test_divisor_substrings()
