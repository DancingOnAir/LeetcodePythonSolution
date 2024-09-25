from typing import List


class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        bannedWords = set(bannedWords)
        return sum(1 for s in message if s in bannedWords) >= 2


def test_report_spam():
    solution = Solution()
    assert solution.reportSpam(["hello","world","leetcode"], ["world","hello"]), 'wrong result'
    assert not solution.reportSpam(["hello","programming","fun"], ["world","programming","leetcode"]), 'wrong result'


if __name__ == '__main__':
    test_report_spam()
