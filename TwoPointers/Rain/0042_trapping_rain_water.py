from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        pre_max = [0] * n
        pre_max[0] = height[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], height[i])

        suf_max = [0] * n
        suf_max[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            suf_max[i] = max(suf_max[i + 1], height[i])

        res = 0
        for h, pre, suf in zip(height, pre_max, suf_max):
            res += min(pre, suf) - h
        return res


def test_trap():
    solution = Solution()
    assert solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6, 'wrong result'
    assert solution.trap([4, 2, 0, 3, 2, 5]) == 9, 'wrong result'


if __name__ == '__main__':
    test_trap()
