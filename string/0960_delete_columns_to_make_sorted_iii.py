from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs[0])
        dp = [1] * m

        for i in range(m - 2, -1, -1):
            for j in range(i + 1, m):
                if all(s[i] <= s[j] for s in strs):
                    dp[i] = max(dp[i], dp[j] + 1)
        return m - max(dp)


def test_min_deletion_size():
    solution = Solution()
    assert solution.minDeletionSize(["babca","bbazb"]) == 3, 'wrong result'
    assert solution.minDeletionSize(["edcba"]) == 4, 'wrong result'
    assert solution.minDeletionSize(["ghi","def","abc"]) == 0, 'wrong result'


if __name__ == '__main__':
    test_min_deletion_size()
