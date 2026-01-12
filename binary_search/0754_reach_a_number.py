from math import ceil


class Solution:
    # math
    # s = n * (n + 1) // 2 >= target
    # if s == target then return n else check n % 2
    # https://leetcode.cn/problems/reach-a-number/solution/fen-lei-tao-lun-xiang-xi-zheng-ming-jian-sqj2/
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        n = ceil(((1 + 8 * target) ** 0.5 - 1) / 2)
        return n if (n * (n + 1) // 2 - target) % 2 == 0 else n + 1 + n % 2


def test_reach_number():
    solution = Solution()
    assert solution.reachNumber(2) == 3, 'wrong result'
    assert solution.reachNumber(3) == 2, 'wrong result'


if __name__ == '__main__':
    test_reach_number()
