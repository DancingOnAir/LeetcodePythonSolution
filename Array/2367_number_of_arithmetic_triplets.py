from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        cnt = [False] * 201
        res = 0
        for x in nums:
            if x >= 2 * diff:
                res += cnt[x - diff] and cnt[x - diff * 2]
            cnt[x] = True
        return res

    def arithmeticTriplets2(self, nums: List[int], diff: int) -> int:
        seen = set()
        res = 0
        for x in nums:
            if x - diff in seen and x - diff * 2 in seen:
                res += 1
            seen.add(x)
        return res

    def arithmeticTriplets1(self, nums: List[int], diff: int) -> int:
        nums = set(nums)
        res = 0
        for x in nums:
            if x + diff in nums and x + diff * 2 in nums:
                res += 1
        return res


def test_arithmetic_triplets():
    solution = Solution()
    assert solution.arithmeticTriplets([0, 1, 4, 6, 7, 10], 3) == 2, 'wrong result'
    assert solution.arithmeticTriplets([4, 5, 6, 7, 8, 9], 2) == 2, 'wrong result'


if __name__ == '__main__':
    test_arithmetic_triplets()
