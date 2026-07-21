class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        MOD = 1_000_000_007
        s = (sum(nums) - 1) // k
        return (s + 1) * s // 2 % MOD


def test_minimum_cost():
    solution = Solution()
    assert solution.minimumCost([1,2,3,4], k = 4) == 3, 'wrong result'
    assert solution.minimumCost([1,1,7,14], k = 4) == 15, 'wrong result'
    assert solution.minimumCost([1,2,3,4], k = 10) == 0, 'wrong result'


if __name__ == '__main__':
    test_minimum_cost()
