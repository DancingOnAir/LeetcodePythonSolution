import string


class Solution:
    # greedy
    def getSmallestString(self, n: int, k: int) -> str:
        k -= n
        res = ['a'] * n
        i = n - 1
        while i >= 0 and k > 0:
            res[i] = chr(ord(res[i]) + min(k, 25))
            k -= min(k, 25)
            i -= 1
        return ''.join(res)

    # math
    def getSmallestString2(self, n: int, k: int) -> str:
        q, r = divmod(k - n, 25)
        return ('' if q == n else 'a' * (n - q - 1) + chr(ord('a') + r)) + 'z' * q

    def getSmallestString1(self, n: int, k: int) -> str:
        def helper(q, r):
            if q + r == n:
                return 'a' * r + 'z' * q
            elif q + r > n:
                num_a = n - q - 1
                return 'a' * num_a + string.ascii_lowercase[r - num_a - 1] + 'z' * q
            else:
                while q + r < n:
                    q -= 1
                    r += 26
                return helper(q, r)

        q, r = divmod(k, 26)
        return helper(q, r)


def test_get_smallest_string():
    solution = Solution()

    assert solution.getSmallestString(3, 27) == 'aay', 'wrong result'
    assert solution.getSmallestString(5, 73) == 'aaszz', 'wrong result'


if __name__ == '__main__':
    test_get_smallest_string()
