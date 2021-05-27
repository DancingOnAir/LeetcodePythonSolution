class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = yx = 0
        for c1, c2 in zip(s1, s2):
            xy += c1 == 'x' and c2 == 'y'
            yx += c1 == 'y' and c2 == 'x'
        return xy // 2 + yx // 2 + xy % 2 + yx % 2 if not ((xy + yx) & 1) else -1

    def minimumSwap1(self, s1: str, s2: str) -> int:
        xy = yx = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == 'x':
                    xy += 1
                else:
                    yx += 1

        if (xy + yx) & 1:
            return -1
        return xy // 2 + yx // 2 + xy % 2 + yx % 2


def test_minimum_swap():
    solution = Solution()
    assert solution.minimumSwap('xx', 'yy') == 1, 'wrong result'
    assert solution.minimumSwap('xy', 'yx') == 2, 'wrong result'
    assert solution.minimumSwap('xx', 'xy') == -1, 'wrong result'
    assert solution.minimumSwap('xxyyxyxyxx', 'xyyxyxxxyx') == 4, 'wrong result'


if __name__ == '__main__':
    test_minimum_swap()
