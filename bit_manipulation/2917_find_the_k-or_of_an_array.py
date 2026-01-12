from typing import List


class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(32):
            cnt = 0
            mask = 1 << i
            for x in nums:
                if x & mask:
                    cnt += 1
                if cnt == k:
                    res += mask
                    break
        return res


def test_find_k_or():
    solution = Solution()
    assert solution.findKOr([7, 12, 9, 8, 9, 15], 4) == 9, 'wrong result'
    assert solution.findKOr([2, 12, 1, 11, 4, 5], 6) == 0, 'wrong result'
    assert solution.findKOr([10, 8, 5, 9, 11, 6, 8], 1) == 15, 'wrong result'


if __name__ == '__main__':
    test_find_k_or()
