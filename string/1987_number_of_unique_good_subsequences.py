class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        mod = 10 ** 9 + 7
        dp = [0] * 2
        for ch in binary:
            dp[int(ch)] = (sum(dp) + int(ch)) % mod
        return (sum(dp) + ('0' in binary)) % mod

    def numberOfUniqueGoodSubsequences1(self, binary: str) -> int:
        zeros = ones = 0
        mod = 10 ** 9 + 7
        for i in binary:
            if i == '1':
                ones = (ones + zeros + 1) % mod
            else:
                zeros = (ones + zeros) % mod
        return (ones + zeros + ('0' in binary)) % mod


def test_number_of_unique_good_subsequences():
    solution = Solution()

    assert solution.numberOfUniqueGoodSubsequences("001") == 2, 'wrong result'
    assert solution.numberOfUniqueGoodSubsequences("11") == 2, 'wrong result'
    assert solution.numberOfUniqueGoodSubsequences("101") == 5, 'wrong result'


if __name__ == '__main__':
    test_number_of_unique_good_subsequences()
