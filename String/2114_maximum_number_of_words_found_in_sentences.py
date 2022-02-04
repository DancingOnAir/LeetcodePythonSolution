from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(len(s.split()) for s in sentences)


def test_most_words_found():
    solution = Solution()
    assert solution.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]) == 6, 'wrong result'
    assert solution.mostWordsFound(["please wait", "continue to fight", "continue to win"]) == 3, 'wrong result'


if __name__ == '__main__':
    test_most_words_found()
