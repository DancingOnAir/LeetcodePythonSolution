class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        mod = 10 ** 9 + 7
        a = min(n, target // 2)
        b = n - a
        return (((a + 1) * a // 2) % mod + ((target + b + target - 1) * b // 2) % mod) % mod
        

def test_minimum_possible_sum():
    solution = Solution()
    assert solution.minimumPossibleSum(2, 3) == 4, 'wrong result'
    assert solution.minimumPossibleSum(3, 3) == 8, 'wrong result'
    assert solution.minimumPossibleSum(1, 1) == 1, 'wrong result'


if __name__ == '__main__':
    test_minimum_possible_sum()