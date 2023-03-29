from typing import List


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        digits = '0123456789'
        d = {c: i for i, c in enumerate(digits)}
        res = [0] * len(word)
        r = 0
        for i, c in enumerate(word):
            num = r * 10 + d[c]
            r = num % m
            if r == 0:
                res[i] = 1
        return res

    def divisibilityArray1(self, word: str, m: int) -> List[int]:
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
