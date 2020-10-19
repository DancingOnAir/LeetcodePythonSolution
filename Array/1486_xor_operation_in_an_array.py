from typing import List


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for i in range(n):
            res ^= (start + 2 * i)
        return res


def test_xor_operation():
    solution = Solution()

    n1 = 5
    start1 = 0
    print(solution.xorOperation(n1, start1))

    n2 = 4
    start2 = 3
    print(solution.xorOperation(n2, start2))

    n3 = 1
    start3 = 7
    print(solution.xorOperation(n3, start3))

    n4 = 10
    start4 = 5
    print(solution.xorOperation(n4, start4))


if __name__ == '__main__':
    test_xor_operation()
