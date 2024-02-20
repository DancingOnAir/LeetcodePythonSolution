from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        res = [0] * n
        idx = -n
        for i, x in enumerate(s):
            if x == c:
                idx = i
            res[i] = i - idx

        idx = n * 2
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                idx = i
            res[i] = min(res[i], idx - i)
        return res


def test_shortest_to_char():
    solution = Solution()
    assert solution.shortestToChar("loveleetcode", "e") == [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0], 'wrong result'
    assert solution.shortestToChar("aaab", "b") == [3, 2, 1, 0], 'wrong result'


if __name__ == '__main__':
    test_shortest_to_char()

