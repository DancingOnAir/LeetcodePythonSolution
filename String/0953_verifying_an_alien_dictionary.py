from typing import List


class Solution:
    def isAlienSorted1(self, words: List[str], order: str) -> bool:
        n = len(words)
        if n == 1:
            return True

        seq = {c: i for i, c in enumerate(order)}
        for i in range(1, n):
            flag = True
            for j in range(min(len(words[i - 1]), len(words[i]))):
                if words[i - 1][j] == words[i][j]:
                    continue
                elif seq[words[i - 1][j]] < seq[words[i][j]]:
                    flag = False
                    break
                elif seq[words[i - 1][j]] > seq[words[i][j]]:
                    return False

            if flag and len(words[i - 1]) > len(words[i]):
                return False
        return True


def test_is_alien_sorted():
    solution = Solution()
    assert solution.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"), 'wrong result'
    assert not solution.isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"), 'wrong result'
    assert not solution.isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz"), 'wrong result'


if __name__ == '__main__':
    test_is_alien_sorted()
