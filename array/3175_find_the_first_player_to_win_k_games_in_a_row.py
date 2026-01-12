from typing import List


class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        pre, cnt = 0, 0
        for i in range(1, len(skills)):
            if skills[pre] < skills[i]:
                pre = i
                cnt = 0
            cnt += 1
            if cnt == k:
                return pre
        return pre


def test_find_winning_player():
    solution = Solution()
    assert solution.findWinningPlayer([4, 2, 6, 3, 9], 2) == 2, 'wrong result'
    assert solution.findWinningPlayer([2, 5, 4], 3) == 1, 'wrong result'


if __name__ == '__main__':
    test_find_winning_player()
