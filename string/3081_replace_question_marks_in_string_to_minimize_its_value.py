from heapq import heappop, heappush, heapreplace, heapify
from collections import Counter
from string import ascii_lowercase


class Solution:
    def minimizeStringValue(self, s: str) -> str:
        freq = Counter(s)
        hp = [(freq[c], c) for c in ascii_lowercase]
        heapify(hp)

        tmp = []
        for _ in range(s.count('?')):
            x, c = hp[0]
            tmp.append(c)
            heapreplace(hp, (x + 1, c))
        tmp.sort()

        res = list(s)
        j = 0
        for i in range(len(s)):
            if s[i] == '?':
                res[i] = tmp[j]
                j += 1

        return ''.join(res)


def test_minimize_string_value():
    solution = Solution()
    assert solution.minimizeStringValue("abcdefghijklmnopqrstuvwxy??") == "abcdefghijklmnopqrstuvwxyaz", 'wrong result'
    assert solution.minimizeStringValue("???") == "abc", 'wrong result'
    assert solution.minimizeStringValue("a?a?") == "abac", 'wrong result'


if __name__ == '__main__':
    test_minimize_string_value()

