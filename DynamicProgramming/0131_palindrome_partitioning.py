from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        dp = [[] for _ in range(n+1)]
        for i in range(n):
            for j in range(i + 1)[::-1]:
                if s[j:i+1] == s[j:i+1][::-1]:
                    if not dp[j]:
                        dp[i+1].append([s[j:i + 1]])
                    else:
                        for k in dp[j]:
                            dp[i+1].append(k + [s[j:i + 1]])
        return dp[n]


def test_partition():
    solution = Solution()
    assert solution.partition('aab') == [["a", "a", "b"], ["aa", "b"]], 'wrong result'
    assert solution.partition('a') == [["a"]], 'wrong result'


if __name__ == '__main__':
    test_partition()
