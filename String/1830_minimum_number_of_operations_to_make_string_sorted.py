class Solution:
    # https://leetcode.com/problems/minimum-number-of-operations-to-make-string-sorted/discuss/1163050/Python-O(26n)-math-solution-explained
    def makeStringSorted(self, s: str) -> int:
        cnt, tot, res, combination_tot = [0] * 26, 0, 0, 1
        for c in s[::-1]:
            idx = ord(c) - 97
            cnt[idx] += 1
            tot += 1

            # eg. 'cdbea' for i == 0, choose 'a' or 'b' is less than 'c', so permutation num is 2 * 4!
            # we can derive that
            # for i, permutation num = sum(cnt[:idx]) * (tot - 1)! / cnt[0]! * cnt[1]! * ... * cnt[idx - 1]
            # equals (sum(cnt[:idx]) / tot) * (tot! / cnt[0]! * cnt[1]! * ... * cnt[idx - 1])
            combination_tot = combination_tot * tot // cnt[idx]
            res += combination_tot * sum(cnt[:idx]) // tot
        return res % (10 ** 9 + 7)

def test_make_string_sorted():
    solution = Solution()
    assert solution.makeStringSorted('cba') == 5, 'wrong result'
    assert solution.makeStringSorted('aabaa') == 2, 'wrong result'
    assert solution.makeStringSorted('cdbea') == 63, 'wrong result'
    assert solution.makeStringSorted('leetcodeleetcodeleetcode') == 982157772, 'wrong result'


if __name__ == '__main__':
    test_make_string_sorted()
