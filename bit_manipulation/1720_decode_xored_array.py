from typing import List
from itertools import accumulate


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        return list(accumulate([first] + encoded, lambda x, y: x ^ y))

    def decode1(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for x in encoded:
            res.append(res[-1] ^ x)
        return res


def test_decode():
    solution = Solution()
    assert solution.decode([1, 2, 3], 1) == [1, 0, 2, 1], 'wrong result'
    assert solution.decode([6, 2, 7, 3], 4) == [4, 2, 0, 7, 4], 'wrong result'


if __name__ == '__main__':
    test_decode()
