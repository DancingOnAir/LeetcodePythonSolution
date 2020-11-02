from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def count(d):
            res, cur = 1, position[0]
            for i in range(1, len(position)):
                if position[i] - cur >= d:
                    res += 1
                    cur = position[i]
            return res

        l, r = 0, position[-1] - position[0]
        while l < r:
            mid = l + (r - l) // 2
            if count(mid) >= m:
                l = mid
            else:
                r = mid - 1

        return l


def test_max_distance():
    solution = Solution()

    position1 = [1, 2, 3, 4, 7]
    m1 = 3
    print(solution.maxDistance(position1, m1))
    assert solution.maxDistance(position1, m1) == 3, "error result"

    position2 = [5, 4, 3, 2, 1, 1000000000]
    m2 = 2
    solution.maxDistance(position2, m2)
    assert solution.maxDistance(position2, m2) == 999999999, "error result"


if __name__ == '__main__':
    test_max_distance()


