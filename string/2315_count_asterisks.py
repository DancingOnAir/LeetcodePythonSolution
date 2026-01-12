class Solution:
    def countAsterisks(self, s: str) -> int:
        return sum(w.count('*') for i, w in enumerate(s.split('|')) if i % 2 == 0)

    def countAsterisks1(self, s: str) -> int:
        res = bars = 0
        for c in s:
            if c == '|':
                bars += 1
            elif c == '*' and bars % 2 == 0:
                res += 1
        return res


def test_count_asterisks():
    solution = Solution()
    assert solution.countAsterisks("l|*e*et|c**o|*de|") == 2, 'wrong result'
    assert solution.countAsterisks("iamprogrammer") == 0, 'wrong result'
    assert solution.countAsterisks("yo|uar|e**|b|e***au|tifu|l") == 5, 'wrong result'


if __name__ == '__main__':
    test_count_asterisks()
