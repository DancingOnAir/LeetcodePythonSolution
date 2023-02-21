from math import lcm


class Solution:
    # https://leetcode.cn/problems/minimize-the-maximum-of-two-arrays/solution/er-fen-da-an-by-endlesscheng-y8fp/
    # 假设最大是m，那么[1, m]有m个整数,除数是d,那么从1到m有n = m - m / d个不能被d整除的数
    # arr1里独享的数，是能被d2整除不能被d1整除的数，为 m / d2 - m / lcm(d1, d2)
    # arr2里独享的数，是能被d1整除不能被d2整除的数，为 m / d1 - m / lcm(d1, d2)
    # 共享的数，为m - m / d1 - m / d2 + m / lcm(d1, d2)
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        l = lcm(divisor1, divisor2)
        # 上界当uniqueCnt1 = uniqueCnt2 = 2时取到，只能取奇数
        left, right = 1, (uniqueCnt1 + uniqueCnt2) * 2 - 1
        while left <= right:
            mid = left + (right - left) // 2
            if mid - mid // divisor1 - mid // divisor2 + mid // l >= max(uniqueCnt1 - mid // divisor2 + mid // l, 0) + max(uniqueCnt2 - mid // divisor1 + mid // l, 0):
                right = mid - 1
            else:
                left = mid + 1
        return left


def test_minimize_set():
    solution = Solution()
    assert solution.minimizeSet(2, 7, 1, 3) == 4, 'wrong result'
    assert solution.minimizeSet(3, 5, 2, 1) == 3, 'wrong result'
    assert solution.minimizeSet(2, 4, 8, 2) == 15, 'wrong result'


if __name__ == '__main__':
    test_minimize_set()

