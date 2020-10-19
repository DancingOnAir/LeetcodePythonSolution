from typing import List


class Solution:
    # https://leetcode.com/problems/xor-operation-in-an-array/discuss/703026/One-liner-O(1)-time-with-no-recursion-and-detailed-explanation
    # bitwise solution
    # tips1: 2a ^ (2a + 1) = 1
    # tips2: ( 0^1^2^...^(a-1) ) ^ (0^1^2^...^b) if we want to get a^(a+1)^...^b
    def xorOperation(self, n: int, start: int) -> int:
        # here is not 2 * (n - 1)
        end = start + 2 * n
        a, b = start // 2, end // 2
        return ((start & 1) * (n & 1)) + \
               ((((a - 1) * (a & 1)) ^ ((a // 2) & 1)) ^ (((b - 1) * (b & 1)) ^ ((b // 2) & 1))) * 2

    # brute force
    def xorOperation1(self, n: int, start: int) -> int:
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
