class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, '', 1)
        return s


def test_remove_occurrences():
    solution = Solution()

    assert solution.removeOccurrences('daabcbaabcbc', 'abc') == 'dab', 'wrong result'
    assert solution.removeOccurrences('axxxxyyyyb', 'xy') == 'ab', 'wrong result'


if __name__ == '__main__':
    test_remove_occurrences()
