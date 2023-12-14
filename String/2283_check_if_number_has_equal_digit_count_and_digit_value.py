from collections import Counter


class Solution:
    def digitCount(self, num: str) -> bool:
        c = Counter(num)
        for i, x in enumerate(num):
            if c[str(i)] != int(x):
                return False

        return True


def test_digit_count():
    solution = Solution()
    assert solution.digitCount("1210"), 'wrong result'
    assert not solution.digitCount("030"), 'wrong result'


if __name__ == '__main__':
    test_digit_count()
