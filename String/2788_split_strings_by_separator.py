from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []

        for word in words:
            for w in word.split(separator):
                if w:
                    res.append(w)

        return res


def test_split_words_by_separator():
    solution = Solution()
    assert solution.splitWordsBySeparator(["one.two.three", "four.five", "six"], ".") == ["one", "two", "three", "four",
                                                                                          "five", "six"], 'wrong result'
    assert solution.splitWordsBySeparator(["$easy$", "$problem$"], "$") == ["easy", "problem"], 'wrong result'


if __name__ == '__main__':
    test_split_words_by_separator()
