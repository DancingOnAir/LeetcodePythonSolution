class Solution:
    def countValidSubstrings(self, s: str) -> int:
        a = b = c = -1
        res = 0
        for i, x in enumerate(s):
            if x == 'a':
                a = i
            elif x == 'b':
                b = a
            elif x == 'c':
                c = b
            res += i - c
        return res


def test_count_valid_substrings():
    solution = Solution()
    assert solution.countValidSubstrings("abac") == 9
    assert solution.countValidSubstrings("abc") == 5
    assert solution.countValidSubstrings("ac") == 3


if __name__ == '__main__':
    test_count_valid_substrings()
