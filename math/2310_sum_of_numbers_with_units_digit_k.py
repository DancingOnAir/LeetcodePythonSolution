class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        mod10 = num % 10
        for i in range(1, 11):
            x = k * i
            if num >= x and mod10 == x % 10:
                return i
        return -1

    def minimumNumbers1(self, num: int, k: int) -> int:
        if num == 0:
            return 0

        unit_digits = dict()
        multiply = k
        i = 1
        while (multiply % 10) not in unit_digits:
            unit_digits[multiply % 10] = i
            multiply += k
            i += 1

        if (num % 10) not in unit_digits:
            return -1
        if unit_digits[num % 10] * k > num:
            return -1
        return unit_digits[num % 10]


def test_minimum_numbers():
    solution = Solution()
    assert solution.minimumNumbers(58, 9) == 2, 'wrong result'
    assert solution.minimumNumbers(37, 2) == -1, 'wrong result'
    assert solution.minimumNumbers(0, 7) == 0, 'wrong result'


if __name__ == '__main__':
    test_minimum_numbers()
