class Solution:
    # https://leetcode.com/problems/bulb-switcher-ii/solutions/107274/2-line-python-recursive-with-explanation/
    # 因为4种按钮，按偶数次相当没有按，所有一共有16种情况(0,0,0,0),(1,0,0,0) ... (1,1,1,1)
    # 由上面的链接可得需要n > 2时，有8种情况
    # presses > 2时，可以实现这8种情况
    def flipLights(self, n: int, presses: int) -> int:
        m, n = min(3, presses), min(3, n)
        return 1 if n == 0 or m == 0 else self.flipLights(n - 1, m) + self.flipLights(n - 1, m - 1)


def test_flip_lights():
    solution = Solution()
    assert solution.flipLights(1, 1) == 2, 'wrong result'
    assert solution.flipLights(2, 1) == 3, 'wrong result'
    assert solution.flipLights(3, 1) == 4, 'wrong result'


if __name__ == '__main__':
    test_flip_lights()
