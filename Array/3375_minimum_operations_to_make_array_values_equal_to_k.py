from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        m = set()
        res = 0
        for x in nums:
            if x not in m:
                m.add(x)
                if x < k:
                    return -1
                elif x > k:
                    res += 1
        return res


def test_min_operations():
    solution = Solution()
    assert solution.minOperations([5, 2, 5, 4, 5], 2) == 2, 'wrong result'
    assert solution.minOperations([2, 1, 2], 2) == -1, 'wrong result'
    assert solution.minOperations([9, 7, 5, 3], 1) == 4, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
