from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        s = set(words)
        for w in words:
            for i in range(1, len(w)):
                s.discard(w[i:])
        return sum(len(w) + 1 for w in s)

    def minimumLengthEncoding1(self, words: List[str]) -> int:
        m = []
        for w1 in sorted(words, key=len)[::-1]:
            for w2 in m:
                if w2.endswith(w1):
                    break
            else:
                m.append(w1)
        return len(m) + len(''.join(m))


def test_minimum_length_encoding():
    solution = Solution()
    assert solution.minimumLengthEncoding(["time", "me", "bell"]) == 10, 'wrong result'
    assert solution.minimumLengthEncoding(["t"]) == 2, 'wrong result'


if __name__ == '__main__':
    test_minimum_length_encoding()
