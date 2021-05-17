class Solution:
    def numSteps(self, s: str) -> int:
        num = 0
        for i, c in enumerate(s[::-1]):
            num += 2 ** i * (c == '1')

        res = 0
        while num != 1:
            if num & 1:
                num += 1
            else:
                num >>= 1
            res += 1

        return res


def test_num_steps():
    solution = Solution()
    assert solution.numSteps('1101') == 6, 'wrong result'
    assert solution.numSteps('10') == 1, 'wrong result'
    assert solution.numSteps('1') == 0, 'wrong result'


if __name__ == '__main__':
    test_num_steps()
