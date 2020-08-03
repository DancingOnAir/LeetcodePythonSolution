class Solution:
    # max_area = max(min(height1, height2) * (x2 - x1))
    def maxArea(self, height: list) -> int:
        n = len(height)

        res = 0
        for i, h1 in enumerate(height):
            for j, h2 in enumerate(height[i + 1:], start=i + 1):
                res = max(res, min(h1, h2) * (j - i))

        return res


def test_max_area():
    solution = Solution()

    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(solution.maxArea(height1))


if __name__ == '__main__':
    test_max_area()
