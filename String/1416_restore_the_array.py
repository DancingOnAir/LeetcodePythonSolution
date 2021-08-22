class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        nums = list()
        i = 0
        while i < len(s):
            j = i + 1
            while j < len(s) and s[j] == '0':
                j += 1
            nums.append(int(s[i: j]))
            i = j

        n = len(nums)
        if nums[0] > k:
            return 0

        dp = [0] * n
        dp[0] = 1

        memo = [nums[0]]

        for i in range(1, n):
            if nums[i] > k:
                return 0

            for j, m in enumerate(memo):
                new_num = m * 10 + nums[i]
                if new_num <= k:
                    memo[j] = new_num

            dp[i] = dp[i - 1] + len(memo)
            memo += [nums[i]] * dp[i - 1]

        return dp[n - 1]


def test_number_of_arrays():
    solution = Solution()

    # assert solution.numberOfArrays("1000", 1000) == 1, 'wrong result'
    # assert solution.numberOfArrays("1000", 10) == 0, 'wrong result'
    assert solution.numberOfArrays("1317", 2000) == 8, 'wrong result'
    assert solution.numberOfArrays("2020", 30) == 1, 'wrong result'
    assert solution.numberOfArrays("1234567890", 90) == 34, 'wrong result'


if __name__ == '__main__':
    test_number_of_arrays()
