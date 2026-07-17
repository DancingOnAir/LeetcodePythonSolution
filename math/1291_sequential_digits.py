class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        res = []
        low_str = str(low)
        high_str = str(high)
        for n in range(len(low_str), len(high_str) + 1):
            for x in range(1, 11 - n):
                cur = 0
                for i in range(n):
                    cur += (x + i) * 10 ** (n - 1 - i)
                if cur > high:
                    break
                if cur >= low:
                    res.append(cur)
        return res


def test_sequential_digits():
    solution = Solution()
    assert solution.sequentialDigits(100, 300) == [123, 234], 'wrong result'
    assert solution.sequentialDigits(1000, 13000) == [1234, 2345, 3456, 4567, 5678, 6789, 12345], 'wrong result'


if __name__ == '__main__':
    test_sequential_digits()

