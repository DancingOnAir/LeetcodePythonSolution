class Solution:
    def findGCD(self, nums: list[int]) -> int:
        def gcd(a: int, b: int) -> int:
            return a if b == 0 else gcd(b, a % b)

        mx = max(nums)
        mn = min(nums)
        return gcd(mx, mn)


def test_find_gcd():
    solution = Solution()
    assert solution.findGCD([2, 5, 6, 9, 10]) == 2, 'wrong result'
    assert solution.findGCD([7, 5, 6, 8, 3]) == 1, 'wrong result'
    assert solution.findGCD([3, 3]) == 3, 'wrong result'


if __name__ == '__main__':
    test_find_gcd()
