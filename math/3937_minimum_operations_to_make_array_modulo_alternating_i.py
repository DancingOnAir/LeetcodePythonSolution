class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        n = len(nums)
        min_ops = [0] * 101
        for x in range(k):
            tot = 0
            for i in range(0, n, 2):
                r = nums[i] % k
                tot += min(abs(r - x), k - abs(r - x))
                min_ops[x] = tot

        res = float('inf')
        for y in range(k):
            tot = 0
            for i in range(1, n, 2):
                r = nums[i] % k
                tot += min(abs(r - y), k - abs(r - y))

            for x in range(k):
                if x != y:
                    res = min(res, tot + min_ops[x])
        return res


def test_min_operations():
    solution = Solution()
    assert solution.minOperations([1, 4, 2, 8], k=3) == 2, 'wrong result'
    assert solution.minOperations([1, 1, 1], k=3) == 1, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
