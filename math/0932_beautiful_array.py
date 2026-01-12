from typing import List


class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        res = [1]
        while len(res) < n:
            res = [i * 2 - 1 for i in res] + [i * 2 for i in res]

        return [i for i in res if i <= n]


def test_beautiful_array():
    solution = Solution()
    assert solution.beautifulArray(4) == [2, 1, 4, 3], 'wrong result'
    assert solution.beautifulArray(5) == [3, 1, 2, 5, 4], 'wrong result'


if __name__ == '__main__':
    test_beautiful_array()
