from typing import List


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        res = list()
        mod = 0
        for i, v in enumerate(word):
            mod = (mod * 10 + int(v)) % m
            res.append(0 if mod else 1)
        return res


def test_divisibility_array():
    solution = Solution()
    assert solution.divisibilityArray("998244353", 3) == [1, 1, 0, 0, 0, 1, 1, 0, 0], 'wrong result'
    assert solution.divisibilityArray("1010", 10) == [0, 1, 0, 1], 'wrong result'


if __name__ == '__main__':
    test_divisibility_array()
