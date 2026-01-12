from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        for x in sorted(dictionary, key=lambda x: (-len(x), x)):
            it = iter(s)
            if all(c in it for c in x):
                return x
        return ""

    def findLongestWord1(self, s: str, dictionary: List[str]) -> str:
        for w in sorted(dictionary, key=lambda x: (-len(x), x)):
            i, j = 0, 0
            while i < len(s):
                if s[i] == w[j]:
                    j += 1
                i += 1

                if j == len(w):
                    return w
        return ""


def test_find_longest_word():
    solution = Solution()
    assert solution.findLongestWord("abce", ["abe", "abc"]) == "abc", 'wrong result'
    assert solution.findLongestWord("abpcplea", ["ale", "apple", "monkey", "plea"]) == "apple", 'wrong result'
    assert solution.findLongestWord("abpcplea", ["a", "b", "c"]) == "a", 'wrong result'


if __name__ == '__main__':
    test_find_longest_word()
