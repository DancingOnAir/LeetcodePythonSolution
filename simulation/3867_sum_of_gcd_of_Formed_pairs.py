class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)

        prefixGcd = []
        mx = 0
        for x in nums:
            mx = max(mx, x)
            prefixGcd.append(gcd(mx, x))
        prefixGcd.sort()
        n = len(prefixGcd)
        return sum(gcd(prefixGcd[i], prefixGcd[-i - 1]) for i in range(n // 2))


def test_gcd_sum():
    solution = Solution()
    assert solution.gcdSum([2,6,4]) == 2, 'wrong result'
    assert solution.gcdSum([3,6,2,8]) == 5, 'wrong result'


if __name__ == '__main__':
    test_gcd_sum()
