class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        acc = 0
        while n > 0:
            r = n % 10
            acc += r * (r - 1)
            if acc >= 50:
                return True
            n = n // 10
        return False


def test_check_good_integer():
    solution = Solution()
    assert not solution.checkGoodInteger(1000), "wrong result"
    assert solution.checkGoodInteger(19), "wrong result"


if __name__ == '__main__':
    test_check_good_integer()
