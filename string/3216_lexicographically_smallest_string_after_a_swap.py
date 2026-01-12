from itertools import pairwise


class Solution:
    def getSmallestString(self, s: str) -> str:
        s = list(s)
        for i, j in pairwise(range(len(s))):
            if s[i] > s[j] and (ord(s[i]) - ord(s[j])) % 2 == 0:
                s[i], s[j] = s[j], s[i]
                break
        return ''.join(s)

    def getSmallestString1(self, s: str) -> str:
        s = list(s)
        for i in range(len(s) - 1):
            if s[i] > s[i + 1] and (int(s[i]) % 2) == (int(s[i + 1]) % 2):
                s[i], s[i + 1] = s[i + 1], s[i]
                return ''.join(s)
        return ''.join(s)


def test_get_smallest_string():
    solution = Solution()
    assert solution.getSmallestString("10") == "10", 'wrong result'
    assert solution.getSmallestString("45320") == "43520", 'wrong result'
    assert solution.getSmallestString("001") == "001", 'wrong result'


if __name__ == '__main__':
    test_get_smallest_string()
