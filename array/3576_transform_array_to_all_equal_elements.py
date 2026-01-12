from typing import List


class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        def check(target):
            cnt = k
            mul = 1
            for i, x in enumerate(nums):
                if x * mul == target:
                    mul = 1
                    continue
                if cnt == 0 or i == len(nums) - 1:
                    return False
                cnt -= 1
                mul = -1
            return True

        return check(1) or check(-1)


def test_can_make_equal():
    solution = Solution()
    assert solution.canMakeEqual([1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1], k=5), 'wrong result'
    assert solution.canMakeEqual([1, -1, 1, -1, 1], k=3), 'wrong result'
    assert not solution.canMakeEqual([-1, -1, -1, 1, 1, 1], k=5), 'wrong result'


if __name__ == '__main__':
    test_can_make_equal()
