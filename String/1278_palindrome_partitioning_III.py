class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        def dfs(s, k):
            if (s, k) in memo:
                return memo[(s, k)]

            if len(s) == k:
                return 0

            if k == 1:
                # -1 - i = ~i
                return sum(s[i] != s[~i] for i in range(len(s) // 2))

            res = float('inf')
            # len(s) - 1 - (k - 1) == len(s) - k + 2
            for i in range(1, len(s) - k + 2):
                res = min(res, dfs(s[:i], 1) + dfs(s[i:], k - 1))

            memo[(s, k)] = res
            return res

        memo = dict()
        return dfs(s, k)

    # TLE top-down dfs
    def palindromePartition1(self, s: str, k: int) -> int:
        def cost(s, i, j):
            r = 0
            while i < j:
                if s[i] != s[j]:
                    r += 1
                i += 1
                j -= 1
            return r

        n = len(s)
        memo = dict()

        def dfs(start, k):
            if (start, k) in memo:
                return memo[(start, k)]

            if n - start == k:
                return 0

            if k == 1:
                return cost(s, start, n - 1)

            res = float('inf')
            for i in range(start + 1, n - k + 2):
                res = min(res, dfs(i, k - 1) + cost(s, start, i - 1))

            memo[(i, k)] = res
            return res

        return dfs(0, k)


def test_palindrome_partition():
    solution = Solution()
    assert solution.palindromePartition("abc", 2) == 1, 'wrong result'
    assert solution.palindromePartition("aabbc", 3) == 0, 'wrong result'
    assert solution.palindromePartition("leetcode", 8) == 0, 'wrong result'


if __name__ == '__main__':
    test_palindrome_partition()
