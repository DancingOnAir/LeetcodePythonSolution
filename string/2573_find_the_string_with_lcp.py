from typing import List
from string import ascii_lowercase


class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        res = [''] * n
        i = 0
        for ch in ascii_lowercase:
            while i < n and res[i]:
                i += 1

            if i >= n:
                break

            for j in range(i, n):
                if lcp[i][j] > 0:
                    res[j] = ch

        if '' in res:
            return ""

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                actual_lcp = 0
                if res[i] == res[j]:

                    if i == n - 1 or j == n - 1:
                        actual_lcp = 1
                    else:
                        actual_lcp = lcp[i + 1][j + 1] + 1

                if lcp[i][j] != actual_lcp:
                    return ""
        return ''.join(res)


def test_find_the_string():
    solution = Solution()
    assert solution.findTheString([[4, 0, 2, 0], [0, 3, 0, 1], [2, 0, 2, 0], [0, 1, 0, 1]]) == "abab", 'wrong result'
    assert solution.findTheString([[4, 3, 2, 1], [3, 3, 2, 1], [2, 2, 2, 1], [1, 1, 1, 1]]) == "aaaa", 'wrong result'
    assert solution.findTheString([[4, 3, 2, 1], [3, 3, 2, 1], [2, 2, 2, 1], [1, 1, 1, 3]]) == "", 'wrong result'


if __name__ == '__main__':
    test_find_the_string()
