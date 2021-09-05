class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        n = len(binary)
        dp = [1] + [0] * (n - 1)

        for i in range(1, n):
            dp[i] = dp[i - 1]
        pass


def test_number_of_uniqu_good_subsequences():
    solution = Solution()

    assert solution.numberOfUniqueGoodSubsequences("001") == 2, 'wrong result'
    assert solution.numberOfUniqueGoodSubsequences("11") == 2, 'wrong result'
    assert solution.numberOfUniqueGoodSubsequences("101") == 5, 'wrong result'


if __name__ == '__main__':
    test_number_of_uniqu_good_subsequences()
