from typing import List


class Solution:
    # 101
    # 011
    # 010
    # 110
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        res, mask = 0, 0
        n = max(nums).bit_length()
        for b in range(n - 1, -1, -1):
            mask |= 1 << b
            cnt = 0
            # -1的二进制全部为1
            and_res = -1
            for x in nums:
                and_res &= x & mask
                if and_res:
                    cnt += 1
                else:
                    and_res = -1
            if cnt > k:
                res |= 1 << b
                mask ^= 1 << b
        return res


def test_min_or_after_operations():
    solution = Solution()
    assert solution.minOrAfterOperations([3, 5, 3, 2, 7], 2) == 3, 'wrong result'
    assert solution.minOrAfterOperations([7, 3, 15, 14, 2, 8], 4) == 2, 'wrong result'
    assert solution.minOrAfterOperations([10, 7, 10, 3, 9, 14, 9, 4], 1) == 15, 'wrong result'


if __name__ == '__main__':
    test_min_or_after_operations()
