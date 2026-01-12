class Solution:

    # 题解 https://cloud.tencent.com/developer/article/1659745
    def lastRemaining(self, n: int) -> int:
        if n == 1:
            return 1
        return 2 * (n // 2) + 2 - 2 * self.lastRemaining(n // 2)


def test_last_remaining():
    solution = Solution()

    assert solution.lastRemaining(9) == 6, 'wrong result'
    assert solution.lastRemaining(1) == 1, 'wrong result'


if __name__ == '__main__':
    test_last_remaining()
