from heapq import heappush, heappop, heapify


class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        hp = []
        for x in nums:
            heappush(hp, x)
            if len(hp) > k:
                heappop(hp)
        return sum(heappop(hp) * max(1, mul - (k - i - 1)) for i in range(k))

    def maxSum1(self, nums: list[int], k: int, mul: int) -> int:
        hp = [-x for x in nums]
        heapify(hp)
        res = 0
        while k > 0:
            x = -heappop(hp)
            if mul > 0:
                res += x * mul
            else:
                res += x
            mul -= 1
            k -= 1
        return res


def test_max_sum():
    solution = Solution()
    assert solution.maxSum([6, 1, 2, 9], k=3, mul=2) == 26, 'wrong result'
    assert solution.maxSum([3, 7, 5, 2], k=2, mul=4) == 43, 'wrong result'
    assert solution.maxSum([4, 4], k=1, mul=1) == 4, 'wrong result'


if __name__ == '__main__':
    test_max_sum()
