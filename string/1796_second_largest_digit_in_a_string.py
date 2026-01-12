class Solution:
    def secondHighest(self, s: str) -> int:
        l = sorted(s)
        first, second = -1, -1
        for c in l:
            if c.isdigit() and first != int(c):
                first, second = int(c), first
        return second

    def secondHighest1(self, s: str) -> int:
        first, second = -1, -1
        for c in s:
            if c.isdigit():
                if first < int(c):
                    first, second = int(c), first
                elif second < int(c) < first:
                    second = int(c)
        return second


def test_second_highest():
    solution = Solution()
    assert solution.secondHighest('dfa12321afd') == 2, 'wrong result'
    assert solution.secondHighest('abc1111') == -1, 'wrong result'
    assert solution.secondHighest('sjhtz8344') == 4, 'wrong result'
    assert solution.secondHighest('ck077') == 0, 'wrong result'


if __name__ == '__main__':
    test_second_highest()
