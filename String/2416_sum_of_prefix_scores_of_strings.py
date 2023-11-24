from typing import List


class Trie:
    def __init__(self):
        self.ch = [None] * 26
        self.visited = 0


class Solution:
    # Trie
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        res = []

        for w in words:
            t = trie
            for c in w:
                i = ord(c) - ord('a')
                if not t.ch[i]:
                    t.ch[i] = Trie()
                t.ch[i].visited += 1
                t = t.ch[i]

        for w in words:
            t = trie
            cur = 0
            for c in w:
                i = ord(c) - ord('a')
                cur += t.ch[i].visited
                t = t.ch[i]
            res.append(cur)

        return res

    # brute force, but TLE
    def sumPrefixScores1(self, words: List[str]) -> List[int]:
        n = len(words)
        res = []

        for w in words:
            cur = 0
            for i in range(1, len(w) + 1):
                pre = w[:i]
                flag = [True] * n
                for j, s in enumerate(words):
                    if flag[j]:
                        if s.startswith(pre):
                            cur += 1
                        else:
                            flag[j] = False
            res.append(cur)
        return res


def test_sum_prefix_scores():
    solution = Solution()
    assert solution.sumPrefixScores(["abc", "ab", "bc", "b"]) == [5, 4, 3, 2], 'wrong result'
    assert solution.sumPrefixScores(["abcd"]) == [4], 'wrong result'


if __name__ == '__main__':
    test_sum_prefix_scores()
