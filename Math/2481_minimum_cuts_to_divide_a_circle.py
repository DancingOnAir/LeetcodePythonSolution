class Solution:
    def numberOfCuts(self, n: int) -> int:
        return n if n & 1 and n > 1 else n // 2


def test_number_of_cuts():
    solution = Solution()
    assert solution.numberOfCuts(4) == 2, 'wrong result'
    assert solution.numberOfCuts(3) == 3, 'wrong result'


if __name__ == '__main__':
    test_number_of_cuts()
