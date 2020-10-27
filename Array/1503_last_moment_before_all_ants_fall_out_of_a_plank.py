from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(max(left or [0]), n - min(right or [n]))

    def getLastMoment1(self, n: int, left: List[int], right: List[int]) -> int:
        left.sort()
        right.sort()

        if not left:
            return n - right[0]
        if not right:
            return left[-1]

        return max(n - right[0], left[-1])


def test_get_last_moment():
    solution = Solution()

    n1 = 4
    left1 = [4, 3]
    right1 = [0, 1]
    print(solution.getLastMoment(n1, left1, right1))

    n2 = 7
    left2 = []
    right2 = [0, 1, 2, 3, 4, 5, 6, 7]
    print(solution.getLastMoment(n2, left2, right2))

    n3 = 6
    left3 = [6]
    right3 = [0]
    print(solution.getLastMoment(n3, left3, right3))


if __name__ == '__main__':
    test_get_last_moment()
