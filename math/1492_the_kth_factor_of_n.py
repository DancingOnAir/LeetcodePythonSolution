class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        cnt = 0
        factors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                cnt += 1
                if i * i != n:
                    factors.append(n // i)
            if cnt == k:
                return i
        if len(factors) < k - cnt:
            return -1
        return factors[cnt - k]


def test_kth_factor():
    solution = Solution()
    assert solution.kthFactor(12, 3) == 3, 'wrong result'
    assert solution.kthFactor(7, 2) == 7, 'wrong result'
    assert solution.kthFactor(4, 4) == -1, 'wrong result'


if __name__ == '__main__':
    test_kth_factor()
