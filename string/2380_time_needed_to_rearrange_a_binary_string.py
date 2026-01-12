class Solution:
    # dp, pre0表示i之前的0， dp[i]表示i时需要的操作数，如果当前ch为'0'，dp[i] = dp[i - 1]
    # 如果ch为'1'，dp[i]可能为之前0的个数，也有可能被前面的1挡住，但是也不能超过它，所以比它后一步到相应的位置,dp[i] = max(pre0[i], dp[i-1] + 1)
    def secondsToRemoveOccurrences(self, s: str) -> int:
        res = pre0 = 0
        for c in s:
            if c == '0':
                pre0 += 1
            elif pre0:
                res = max(res + 1, pre0)
        return res


def test_seconds_to_remove_occurrences():
    solution = Solution()
    assert solution.secondsToRemoveOccurrences("0110101") == 4, 'wrong result'
    assert solution.secondsToRemoveOccurrences("11100") == 0, 'wrong result'


if __name__ == '__main__':
    test_seconds_to_remove_occurrences()
