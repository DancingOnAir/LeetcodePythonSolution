from typing import List


class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        base = 10 ** ((intLength - 1) // 2)
        res = [-1] * len(queries)
        for i, q in enumerate(queries):
            if q <= 9 * base:
                s = str(base + q - 1)
                s += s[::-1][intLength % 2:]
                res[i] = int(s)

        return res


def test_kth_palindrome():
    solution = Solution()
    assert solution.kthPalindrome([1, 2, 3, 4, 5, 90], 3) == [101, 111, 121, 131, 141, 999], 'wrong result'
    assert solution.kthPalindrome([2, 4, 6], 4) == [1111, 1331, 1551], 'wrong result'


if __name__ == '__main__':
    test_kth_palindrome()
