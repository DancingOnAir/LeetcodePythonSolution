from string import ascii_uppercase


class Solution:
    def greatestLetter(self, s: str) -> str:
        s = set(s)
        for c in ascii_uppercase[::-1]:
            if c in s and c.swapcase() in s:
                return c
        return ''

    def greatestLetter1(self, s: str) -> str:
        res = ""
        m = set()
        for c in s:
            if c in m:
                if not res or res < c.upper():
                    res = c.upper()
            m.add(c.swapcase())
        return res


def test_greatest_letter():
    solution = Solution()
    assert solution.greatestLetter("lEeTcOdE") == "E", 'wrong result'
    assert solution.greatestLetter("arRAzFif") == "R", 'wrong result'
    assert solution.greatestLetter("AbCdEfGhIjK") == "", 'wrong result'


if __name__ == '__main__':
    test_greatest_letter()
