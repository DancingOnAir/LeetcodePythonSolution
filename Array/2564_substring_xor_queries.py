from typing import List


class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
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
