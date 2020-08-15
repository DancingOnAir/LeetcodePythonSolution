from typing import List


class Solution:
    # stack
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        idx, res = 0, 0
        stack = []
        while idx < len(height):
            while stack and height[idx] > height[stack[-1]]:
                top = stack.pop()
                if not len(stack):
                    break
                h = min(height[stack[-1]], height[idx]) - height[top]
                dist = idx - stack[-1] - 1

                res += dist * h

            stack.append(idx)
            idx += 1
        return res

    # math calculates area
    def trap1(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        left_max, right_max, res = 0, 0, 0
        for i in range(len(height)):
            left_max = max(left_max, height[i])
            right_max = max(right_max, height[-1 - i])
            res += left_max + right_max - height[i]
        return res - left_max * len(height)

    # two pointer
    def trap2(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        res = 0
        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                res += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                res += right_max - height[right]
                right -= 1

        return res

    # brute force but TLE
    def trap3(self, height: List[int]) -> int:
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
