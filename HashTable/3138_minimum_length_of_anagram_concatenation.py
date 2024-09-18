from collections import Counter


class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                cur = Counter(s[:i])
                for j in range(i * 2, n + 1, i):
                    if Counter(s[j - i: j]) != cur:
                        break
                else:
                    return i
        return n


def test_min_anagram_length():
    solution = Solution()
    assert solution.minAnagramLength("abba") == 2, 'wrong result'
    assert solution.minAnagramLength("cdef") == 4, 'wrong result'


if __name__ == '__main__':
    test_min_anagram_length()
