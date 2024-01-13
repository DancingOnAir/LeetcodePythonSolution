class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        res = 1
        cur = a
        while len(cur) < len(b):
            cur += a
            res += 1
        cur += a

        idx = cur.find(b)
        if idx == -1:
            return -1
        return res + 1 if idx + len(b) > len(a) * res else res


def test_repeated_string_match():
    solution = Solution()
    assert solution.repeatedStringMatch("abcd", "cdabcdab") == 3, 'wrong result'
    assert solution.repeatedStringMatch("a", "aa") == 2, 'wrong result'


if __name__ == '__main__':
    test_repeated_string_match()
