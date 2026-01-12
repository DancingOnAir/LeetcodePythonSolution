from typing import List
from functools import reduce
from itertools import accumulate


class Solution:
    # 和下面的方法类似，不过首先计算的是第一个数
    # https://leetcode.com/problems/decode-xored-permutation/solutions/1031107/java-c-python-straight-forward-solution/
    def decode(self, encoded: List[int]) -> List[int]:
        first = reduce(lambda a, b: a ^ b, encoded[::-2] + list(range(len(encoded) + 2)))
        return list(accumulate([first] + encoded, lambda a, b: a ^ b))

    # 先计算全部的xor值, 再计算encoded里的偶数项的xor值, 2者的xor就是原数组最后的元素值。
    # e.g. 原数组[a, b, c, d, e], 那么encoded为[a^b, b^c, c^d, d^e],可以观察到encoded的偶然项的xor为a^b^c^d
    def decode1(self, encoded: List[int]) -> List[int]:
        n = len(encoded)
        total_xor = reduce(lambda a, b: a ^ b, [i for i in range(1, n + 2)])
        res = [0] * (n + 1)
        for i in range(0, n, 2):
            total_xor ^= encoded[i]
        res[-1] = total_xor

        for i in range(n - 1, -1, -1):
            res[i] = encoded[i] ^ res[i + 1]
        return res


def test_decode():
    solution = Solution()
    assert solution.decode([3, 1]) == [1, 2, 3], 'wrong result'
    assert solution.decode([6, 5, 4, 6]) == [2, 4, 1, 5, 3], 'wrong result'


if __name__ == '__main__':
    test_decode()
