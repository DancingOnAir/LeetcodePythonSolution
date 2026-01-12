from typing import List


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        res = [0] * n
        mx = 2 ** maximumBit - 1
        for i in range(len(nums)):
            mx ^= nums[i]
            res[n - i - 1] = mx
        return res

    def getMaximumXor1(self, nums: List[int], maximumBit: int) -> List[int]:
        res = list()
        max_num = 2 ** maximumBit - 1
        acc = 0
        for x in nums:
            acc ^= x
            # 下面2种方法均可
            # res.append(max_num - acc)
            res.append(max_num ^ acc)
        return res[::-1]


def test_get_maximum_xor():
    solution = Solution()
    assert solution.getMaximumXor([0, 1, 1, 3], 2) == [0, 3, 2, 3], 'wrong result'
    assert solution.getMaximumXor([2, 3, 4, 7], 3) == [5, 2, 6, 5], 'wrong result'
    assert solution.getMaximumXor([0, 1, 2, 2, 5, 7], 3) == [4, 3, 6, 4, 6, 7], 'wrong result'


if __name__ == '__main__':
    test_get_maximum_xor()
