class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def helper(num):
            waves = 0
            digits = list(map(int, str(num)))
            for i in range(1, len(digits) - 1):
                if (digits[i - 1] > digits[i] and digits[i + 1] > digits[i]) or (digits[i - 1] < digits[i] and digits[i + 1] < digits[i]):
                    waves += 1
            return waves

        return sum(helper(x) for x in range(num1, num2 + 1))


def test_total_waviness():
    solution = Solution()
    assert solution.totalWaviness(120, 130) == 3, 'wrong result'
    assert solution.totalWaviness(198, 202) == 3, 'wrong result'
    assert solution.totalWaviness(4848, 4848) == 2, 'wrong result'


if __name__ == '__main__':
    test_total_waviness()

