from collections import defaultdict


class Solution:
    def calculateScore(self, s: str) -> int:
        cnt = defaultdict(list)
        res = 0
        for i, c in enumerate(map(ord, s)):
            c -= ord('a')
            if cnt[25 - c]:
                res += i - cnt[25 - c].pop()
            else:
                cnt[c].append(i)

        return res


def test_calculate_score():
    solution = Solution()
    assert solution.calculateScore("aczzx") == 5, 'wrong result'
    assert solution.calculateScore("abcdef") == 0, 'wrong result'


if __name__ == '__main__':
    test_calculate_score()
