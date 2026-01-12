class Solution:
    # max_area = max(min(height1, height2) * (x2 - x1))
    def maxArea(self, height: list) -> int:
        left, right = 0, len(height) - 1
        res = 0

        while left < right:
            if height[left] < height[right]:
                area = height[left] * (right - left)
                left += 1
            else:
                area = height[right] * (right - left)
                right -= 1
            res = max(res, area)
        return res


def test_max_area():
    solution = Solution()

    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(solution.maxArea(height1))


if __name__ == '__main__':
    test_max_area()
