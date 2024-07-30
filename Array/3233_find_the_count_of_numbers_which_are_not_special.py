class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        # Find Upper Limit for Primes: We only need to find primes up to sqrt(r)
        # because we are interested in their squares, which should fall within the range [l, r].
        mx = int(r ** 0.5)
        is_prime = [True] * (mx + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(mx ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, mx + 1, i):
                    is_prime[j] = False

        special_cnt = 0
        for i in range(2, mx + 1):
            if is_prime[i]:
                if l <= i * i <= r:
                    special_cnt += 1
        return r - l + 1 - special_cnt

    # TLE
    def nonSpecialCount1(self, l: int, r: int) -> int:
        def helper(x):
            ans = 0
            for i in range(2, x):
                if x % i == 0:
                    ans += 1
            return ans

        res = 0
        for i in range(l, r + 1):
            if helper(i) != 1:
                res += 1
        return res


def test_non_special_count():
    solution = Solution()
    assert solution.nonSpecialCount(5, 7) == 3, 'wrong result'
    assert solution.nonSpecialCount(4, 16) == 11, 'wrong result'


if __name__ == '__main__':
    test_non_special_count()
