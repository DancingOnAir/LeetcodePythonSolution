from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_val = max(candies)

        return [i + extraCandies >= max_val for i in candies]


def test_kids_with_candies():
    solution = Solution()

    candies1 = [2, 3, 5, 1, 3]
    extraCandies1 = 3
    print(solution.kidsWithCandies(candies1, extraCandies1))

    candies2 = [4, 2, 1, 1, 2]
    extraCandies2 = 1
    print(solution.kidsWithCandies(candies2, extraCandies2))

    candies3 = [12, 1, 12]
    extraCandies3 = 10
    print(solution.kidsWithCandies(candies3, extraCandies3))


if __name__ == '__main__':
    test_kids_with_candies()
