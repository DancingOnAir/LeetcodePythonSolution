from typing import List
from collections import defaultdict


class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        n = len(s)
        seen = defaultdict(lambda: [-1, -1])
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                seen[0] = [i, i]
                continue

            v = 0
            for j in range(i, n):
                v = v * 2 + int(s[j])
                if v > 2 ** 32:
                    break
                seen[v] = [i, j]
        return [seen[a ^ b] for a, b in queries]

    # brute force
    def substringXorQueries1(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        res = list()
        for a, b in queries:
            cur = bin(a ^ b)[2:]
            i = s.find(cur)
            res += [[-1, -1]] if i < 0 else [[i, i + len(cur) - 1]]

        return res


def test_substring_xor_queries():
    solution = Solution()
    assert solution.substringXorQueries("101101", [[0, 5], [1, 2]]) == [[0, 2], [2, 3]], 'wrong result'
    assert solution.substringXorQueries("0101", [[12, 8]]) == [[-1, -1]], 'wrong result'


if __name__ == '__main__':
    test_substring_xor_queries()
