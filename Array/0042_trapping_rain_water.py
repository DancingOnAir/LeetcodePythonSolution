from typing import List


class Solution:
    # brute force but TLE
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        res = 0

        for i in range(1, len(height) - 1):
            max_left, max_right = 0, 0
            for j in range(i + 1):
                max_left = max(max_left, height[j])

            for k in range(i, len(height)):
                max_right = max(max_right, height[k])
            res += min(max_left, max_right) - height[i]
        return res


def test_trap():
    solution = Solution()

    height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(solution.trap(height1))


if __name__ == '__main__':
    test_trap()
