class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 1
        for i in range(len(word) - 1):
            if word[i] == word[i + 1]:
                res += 1
        return res

    def possibleStringCount1(self, word: str) -> int:
        res, cnt = 1, 0
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                cnt += 1
            else:
                res += cnt
                cnt = 0
        return res + cnt


def test_possible_string_count():
    solution = Solution()
    assert solution.possibleStringCount("abbcccc") == 5, 'wrong result'
    assert solution.possibleStringCount("abcd") == 1, 'wrong result'


if __name__ == '__main__':
    test_possible_string_count()
