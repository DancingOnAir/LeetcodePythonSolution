from typing import List


class Solution:
    # Hacker's delight book
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        def get_next_same_pop_out(a):
            if a == 0:
                return (1 << 10) - 1
            c = a & -a
            r = a + c
            return (((r ^ a) >> 2) // c) | r

        res = 0
        i = (1 << k) - 1
        while i < len(nums):
            res += nums[i]
            i = get_next_same_pop_out(i)
        return res

    # brute force
    def sumIndicesWithKSetBits1(self, nums: List[int], k: int) -> int:
        res = 0
        for i, v in enumerate(nums):
            if bin(i)[2:].count('1') == k:
                res += v
        return res


def test_sum_indices_with_k_set_bits():
    solution = Solution()
    assert solution.sumIndicesWithKSetBits([5, 10, 1, 5, 2], 1) == 13, 'wrong result'
    assert solution.sumIndicesWithKSetBits([4, 3, 2, 1], 2) == 1, 'wrong result'


if __name__ == '__main__':
    test_sum_indices_with_k_set_bits()
