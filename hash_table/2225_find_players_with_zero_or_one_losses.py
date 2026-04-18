from collections import defaultdict


class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        winners = set()
        losers = set()
        cnt = defaultdict(int)
        for w, l in matches:
            winners.add(w)
            losers.add(l)
            cnt[l] += 1

        return [sorted(winners - losers), sorted(k for k, v in cnt.items() if v == 1)]


def test_find_winners():
    solution = Solution()
    assert solution.findWinners([[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]) == [
        [1, 2, 10], [4, 5, 7, 8]], 'wrong result'
    assert solution.findWinners([[2, 3], [1, 3], [5, 4], [6, 4]]) == [[1, 2, 5, 6], []], 'wrong result'


if __name__ == '__main__':
    test_find_winners()
