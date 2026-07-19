class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n


def test_gcd_of_odd_and_even_sums():
    solution = Solution()
    assert solution.gcdOfOddEvenSums(4) == 4, 'wrong result'
    assert solution.gcdOfOddEvenSums(5) == 5, 'wrong result'


if __name__ == '__main__':
    test_gcd_of_odd_and_even_sums()
