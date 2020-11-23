from typing import List


class Solution:
    # https://leetcode.com/problems/decode-ways-ii/discuss/105258/Java-O(N)-by-General-Solution-for-all-DP-problems
    # dp[i] --> number of all possible decode ways of substring s(0 : i-1).
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 9 if s[0] == '*' else 1

        for i in range(2, len(s) + 1):
            first = s[i - 2]
            second = s[i - 1]

            # for dp[i - 1]
            if second == '*':
                dp[i] += 9 * dp[i - 1]
            elif second > '0':
                dp[i] += dp[i - 1]

            # for dp[i - 2]
            if first == '*':
                if second == '*':
                    dp[i] += 15 * dp[i - 2]
                elif second < '7':
                    dp[i] += 2 * dp[i - 2]
                else:
                    dp[i] += dp[i - 2]
            elif first == '1' or first == '2':
                if second == '*':
                    if first == '1':
                        dp[i] += 9 * dp[i - 2]
                    else:
                        dp[i] += 6 * dp[i - 2]
                elif (10 * int(first) + int(second)) < 27:
                    dp[i] += dp[i - 2]
            dp[i] %= 10 ** 9 + 7

        return dp[len(s)]


def test_num_decodings():
    solution = Solution()

    assert solution.numDecodings('0') == 0, "wrong result"
    assert solution.numDecodings('*') == 9, "wrong result"
    assert solution.numDecodings('1*') == 18, "wrong result"
    # 1 letter: 21...26, 2 letters: 2, 1; 2, 2; ... ; 2, 9
    assert solution.numDecodings('2*') == 15, "wrong result"
    # 2 letters: 3, 1; 3, 2; ... ; 3, 9
    assert solution.numDecodings('3*') == 9, "wrong result"
    # 2 letters: 10, 1; 10, 2; ... ; 10, 9
    assert solution.numDecodings('10*') == 9, "wrong result"


if __name__ == '__main__':
    test_num_decodings()
