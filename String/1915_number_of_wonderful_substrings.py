from collections import Counter


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        n = len(word)
        if n < 2:
            return n

        res = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                if sum(1 if v & 1 else 0 for v in Counter(word[i: j]).values()) > 1:
                    continue
                res += 1
        return res


def test_wonderful_substrings():
    solution = Solution()

    assert solution.wonderfulSubstrings("aba") == 4, 'wrong result'
    assert solution.wonderfulSubstrings("aabb") == 9, 'wrong result'
    assert solution.wonderfulSubstrings("he") == 2, 'wrong result'


if __name__ == '__main__':
    test_wonderful_substrings()
