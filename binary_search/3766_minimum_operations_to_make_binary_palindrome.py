from typing import List
from bisect import bisect_left


class Solution:
    def minOperations(self, nums: List[int]) -> List[int]:
        def helper():
            MX = 6000
            p = [0]
            pow2 = 1
            while True:
                for i in range(pow2, pow2 * 2):
                    s = bin(i)[2:]
                    x = int(s + s[::-1][1:], 2)
                    if x > MX:
                        return p
                    p.append(x)

                for i in range(pow2, pow2 * 2):
                    s = bin(i)[2:]
                    x = int(s + s[::-1], 2)
                    if x > MX:
                        return p
                    p.append(x)
                pow2 *= 2

        p = helper()
        res = []
        for x in nums:
            i = bisect_left(p, x)
            res.append(min(p[i] - x, x - p[i - 1]))

        return res


def test_min_operations():
    solution = Solution()
    assert solution.minOperations([1, 2, 4]) == [0, 1, 1], 'wrong result'
    assert solution.minOperations([6, 7, 12]) == [1, 0, 3], 'wrong result'


if __name__ == '__main__':
    test_min_operations()
