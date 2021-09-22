class Solution:
    def maxProduct(self, s: str) -> int:
        def manachers(S):
            A = '@#' + '#'.join(S) + '#$'
            Z = [0] * len(A)
            center = right = 0
            for i in range(1, len(A) - 1):
                if i < right:
                    Z[i] = min(right - i, Z[2 * center - i])
                while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
                    Z[i] += 1
                if i + Z[i] > right:
                    center, right = i, i + Z[i]
            return Z[2: -2: 2]

        # def helper(s):
        #     man, n = manachers(s), len(s)
        #     ints =
        pass


def test_max_product():
    solution = Solution()

    assert solution.maxProduct("ababbb") == 9, 'wrong result'
    assert solution.maxProduct("zaaaxbbby") == 9, 'wrong result'


if __name__ == '__main__':
    test_max_product()
