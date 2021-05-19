class Solution:
    def generateTheString(self, n: int) -> str:
        return 'ab'[n & 1] * (n - 1) + 'b'

    def generateTheString1(self, n: int) -> str:
        if n & 1:
            return 'a' * n
        return 'a' * (n - 1) + 'b'


def test_generate_the_string():
    solution = Solution()
    assert solution.generateTheString(4) == 'aaab', 'wrong result'
    assert solution.generateTheString(2) == 'ab', 'wrong result'
    assert solution.generateTheString(7) == 'aaaaaaa', 'wrong result'


if __name__ == '__main__':
    test_generate_the_string()
