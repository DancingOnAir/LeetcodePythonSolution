from collections import Counter


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        c = Counter(s)
        return '1' * (c['1'] - 1) + '0' * c['0'] + '1'


def test_maximum_odd_binary_number():
    solution = Solution()
    assert solution.maximumOddBinaryNumber("010") == "001", 'wrong result'
    assert solution.maximumOddBinaryNumber("0101") == "1001", 'wrong result'


if __name__ == '__main__':
    test_maximum_odd_binary_number()
