from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        def get_max_length(length: int, cuts: List[int]) -> int:
            cuts.sort()
            max_length = max(cuts[0], length - cuts[-1])
            for i in range(1, len(cuts)):
                max_length = max(max_length, cuts[i] - cuts[i-1])
            return max_length
        return get_max_length(h, horizontalCuts) * get_max_length(w, verticalCuts) % 1000000007


def test_max_area():
    solution = Solution()

    h1 = 5
    w1 = 4
    horizontalCuts1 = [1, 2, 4]
    verticalCuts1 = [1, 3]
    print(solution.maxArea(h1, w1, horizontalCuts1, verticalCuts1))

    h2 = 5
    w2 = 4
    horizontalCuts2 = [3, 1]
    verticalCuts2 = [1]
    print(solution.maxArea(h2, w2, horizontalCuts2, verticalCuts2))

    h3 = 5
    w3 = 4
    horizontalCuts3 = [3]
    verticalCuts3 = [3]
    print(solution.maxArea(h3, w3, horizontalCuts3, verticalCuts3))


if __name__ == '__main__':
    test_max_area()
