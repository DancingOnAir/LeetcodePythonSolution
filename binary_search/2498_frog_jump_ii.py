from typing import List


class Solution:
    def maxJump(self, stones: List[int]) -> int:
        def helper(k):
            seen = set()
            cur = pre = 0
            while cur < len(stones):
                if stones[cur] - stones[pre] > k:
                    if cur - 1 == pre:
                        return False
                    pre = cur - 1
                    seen.add(pre)
                cur += 1

            cur = pre = len(stones) - 1
            seen.add(pre)
            while cur >= 0:
                if cur in seen:
                    cur -= 1
                    continue

                if stones[pre] - stones[cur] <= k:
                    pre = cur
                else:
                    return False
                cur -= 1
            return True

        l, r = 0, 10 ** 9
        while l <= r:
            mid = l + (r - l) // 2
            if helper(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l

    def maxJump1(self, stones: List[int]) -> int:
        if len(stones) <= 2:
            return stones[1] - stones[0]
        res = 0
        for i in range(len(stones) - 2):
            res = max(res, stones[i + 2] - stones[i])
        return res


def test_max_jump():
    solution = Solution()
    assert solution.maxJump([0, 2, 5, 6, 7]) == 5, 'wrong result'
    assert solution.maxJump([0, 3, 9]) == 9, 'wrong result'


if __name__ == '__main__':
    test_max_jump()
