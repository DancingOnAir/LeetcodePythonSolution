from math import comb


class Solution:
    def countValidSequences(self, n: int, k: int) -> int:
        res = comb(n - 1, k - 1)
        if (n + k) % 2 == 0:
            res -= comb((n + k) // 2 - 1, k - 1)
        return res % 1_000_000_007


def test_count_valid_sequences():
    solution = Solution()
    assert solution.countValidSequences(5, 3) == 3, 'wrong result'
    assert solution.countValidSequences(3, 2) == 2, 'wrong result'
    assert solution.countValidSequences(5, 5) == 0, 'wrong result'


if __name__ == '__main__':
    test_count_valid_sequences()


