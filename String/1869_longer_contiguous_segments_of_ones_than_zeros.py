from itertools import groupby


class Solution:
    # generic solution
    def checkZeroOnes(self, s: str) -> bool:
        cnt = {0: 0, 1: 0}
        i = j = 0
        while j < len(s):
            while i < len(s) and s[i] == s[j]:
                i += 1
                cnt[ord(s[j]) - ord('0')] = max(cnt[ord(s[j]) - ord('0')], i - j)

            j = i
        return cnt[0] < cnt[1]

    def checkZeroOnes3(self, s: str) -> bool:
        best_zeros = best_ones = cur_zeros = cur_ones = 0
        for c in s:
            if c == '0':
                cur_zeros += 1
                cur_ones = 0
            else:
                cur_ones += 1
                cur_zeros = 0
            best_zeros = max(best_zeros, cur_zeros)
            best_ones = max(best_ones, cur_ones)
        return best_zeros < best_ones

    def checkZeroOnes2(self, s: str) -> bool:
        pre = ''
        zeros = ones = 0
        cur_zeros = cur_ones = 0

        for c in s:
            if not pre or c != pre:
                pre = c
                if c == '0':
                    cur_zeros = 1
                else:
                    cur_ones = 1
            elif c == pre:
                if c == '0':
                    cur_zeros += 1
                else:
                    cur_ones += 1
            zeros = max(zeros, cur_zeros)
            ones = max(ones, cur_ones)

        return zeros < ones

    def checkZeroOnes1(self, s: str) -> bool:
        cnt = [[k, len(list(g))] for k, g in groupby(s)]

        zeros = ones = 0
        for i in cnt:
            if i[0] == '0' and i[1] > zeros:
                zeros = i[1]
            elif i[0] == '1' and i[1] > ones:
                ones = i[1]

        return zeros < ones


def test_check_zero_ones():
    solution = Solution()

    assert solution.checkZeroOnes('1101'), 'wrong result'
    assert not solution.checkZeroOnes('111000'), 'wrong result'
    assert not solution.checkZeroOnes('110100010'), 'wrong result'


if __name__ == '__main__':
    test_check_zero_ones()
