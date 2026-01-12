from typing import List
from collections import Counter


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res, cnt = [], []
        m = set()

        for w in words:
            val = ''.join(sorted(w))
            if val not in m or val != cnt[-1]:
                cnt.append(val)
                res.append(w)
            m.add(val)
        return res

    def removeAnagrams1(self, words: List[str]) -> List[str]:
        res = []
        for i in range(len(words)):
            if not res or Counter(res[-1]) != Counter(words[i]):
                res.append(words[i])
        return res


def test_remove_anagrams():
    solution = Solution()
    assert solution.removeAnagrams(["a", "b", "a"]) == ["a", "b", "a"], 'wrong result'
    assert solution.removeAnagrams(["az", "azz"]) == ["az", "azz"], 'wrong result'
    assert solution.removeAnagrams(["abba", "baba", "bbaa", "cd", "cd"]) == ["abba", "cd"], 'wrong result'
    assert solution.removeAnagrams(["a", "b", "c", "d", "e"]) == ["a", "b", "c", "d", "e"], 'wrong result'


if __name__ == '__main__':
    test_remove_anagrams()
