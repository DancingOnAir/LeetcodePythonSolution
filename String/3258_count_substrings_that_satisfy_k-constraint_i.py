class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        l = res = 0
        ones = zeros = 0
        for r, c in enumerate(s):
            if c == '0':
                zeros += 1
            else:
                ones += 1

            while zeros > k and ones > k:
                if s[l] == '0':
                    zeros -= 1
                else:
                    ones -= 1
                l += 1

            res += r - l + 1
        return res


def test_count_k_constraint_substrings():
    solution = Solution()
    assert solution.countKConstraintSubstrings("10101", 1) == 12, 'wrong result'
    assert solution.countKConstraintSubstrings("1010101", 2) == 25, 'wrong result'
    assert solution.countKConstraintSubstrings("11111", 1) == 15, 'wrong result'


if __name__ == '__main__':
    test_count_k_constraint_substrings()
