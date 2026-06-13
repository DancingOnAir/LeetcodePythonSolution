from typing import List


class Node:
    def __init__(self):
        self.children = dict()
        self.isEnd = 0


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        p = self.root
        for ch in word:
            if ch not in p.children:
                p.children[ch] = Node()
            p = p.children[ch]
        p.isEnd += 1

    def query(self, word):
        p = self.root
        for ch in word:
            if ch not in p.children:
                return False
            p = p.children[ch]
        return True


class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        trie = Trie()
        for w in words:
            trie.insert(w)

        n = len(target)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(n):
            p = trie.root
            for j in range(i, n):
                if target[j] not in p.children:
                    break
                dp[j + 1] = min(dp[j + 1], dp[i] + 1)
                p = p.children[target[j]]
        return dp[-1] if dp[-1] < float('inf') else -1


def test_min_valid_strings():
    solution = Solution()
    assert solution.minValidStrings(["abc","aaaaa","bcdef"], "aabcdabc") == 3, 'wrong result'
    assert solution.minValidStrings(["abababab","ab"], "ababaababa") == 2, 'wrong result'
    assert solution.minValidStrings(["abcdef"], "xyz") == -1, 'wrong result'


if __name__ == '__main__':
    test_min_valid_strings()
