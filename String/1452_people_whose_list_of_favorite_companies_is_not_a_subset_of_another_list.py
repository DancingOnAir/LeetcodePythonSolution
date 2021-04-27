from typing import List
from collections import Counter


class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        favoriteCompanies = [(val, i) for i, val in enumerate(favoriteCompanies)]
        favoriteCompanies.sort(key=lambda x: len(x[0]))
        favoriteCompanies.reverse()
        max_len = len(favoriteCompanies[0][0])
        memo = [Counter(favoriteCompanies[0][0])]
        res = [favoriteCompanies[0][1]]

        for companies in favoriteCompanies[1:]:
            cur_counter = Counter(companies[0])
            if len(companies) == max_len:
                res.append(companies[1])
                memo.append(cur_counter)
                break

            flag = True
            for c in memo:
                if not len(cur_counter - c):
                    flag = False
                    break

            if flag:
                res.append(companies[1])
                memo.append(cur_counter)
        return sorted(res)


def test_people_indexes():
    solution = Solution()

    assert solution.peopleIndexes(
        [["leetcode", "google", "facebook"], ["google", "microsoft"], ["google", "facebook"], ["google"],
         ["amazon"]]) == [0, 1, 4], 'wrong result'
    assert solution.peopleIndexes(
        [["leetcode", "google", "facebook"], ["leetcode", "amazon"], ["facebook", "google"]]) == [0, 1], 'wrong result'
    assert solution.peopleIndexes(
        [["leetcode"], ["google"], ["facebook"], ["amazon"]]) == [0, 1, 2, 3], 'wrong result'


if __name__ == '__main__':
    test_people_indexes()
