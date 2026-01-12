from typing import List
from collections import defaultdict


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        if len(rating) < 3:
            return 0

        less, greater = defaultdict(int), defaultdict(int)
        res = 0
        for i in range(len(rating) - 1):
            for j in range(i + 1, len(rating)):
                if rating[j] > rating[i]:
                    greater[i] += 1
                else:
                    less[i] += 1

        for i in range(len(rating) - 2):
            for j in range(i + 1, len(rating)):
                if rating[i] < rating[j]:
                    res += greater[j]
                else:
                    res += less[j]
        return res


def test_num_teams():
    solution = Solution()

    rating1 = [2, 5, 3, 4, 1]
    print(solution.numTeams(rating1))

    rating2 = [2, 1, 3]
    print(solution.numTeams(rating2))

    rating3 = [1, 2, 3, 4]
    print(solution.numTeams(rating3))


if __name__ == '__main__':
    test_num_teams()
