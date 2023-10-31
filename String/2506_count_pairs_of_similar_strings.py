from typing import List


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        res = 0
        n = len(words)
        words = list(map(set, words))
        for i in range(n):
            for j in range(i + 1, n):
                if len(words[i]) == len(words[j]) == len(words[i] & words[j]):
                    res += 1
        return res


def test_similar_pairs():
    solution = Solution()
    assert solution.similarPairs(["aba", "aabb", "abcd", "bac", "aabc"]) == 2, 'wrong result'
    assert solution.similarPairs(["aabb", "ab", "ba"]) == 3, 'wrong result'
    assert solution.similarPairs(["nba", "cba", "dba"]) == 0, 'wrong result'


if __name__ == '__main__':
    test_similar_pairs()
