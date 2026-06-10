class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        return sum(x for x in range(max(0, n - k), n + k + 1) if (x & n) == 0)


def test_sum_of_good_integers():
    solution = Solution()
    assert solution.sumOfGoodIntegers(2, 3) == 10, 'wrong result'
    assert solution.sumOfGoodIntegers(5, 1) == 0, 'wrong result'


if __name__ == '__main__':
    test_sum_of_good_integers()
