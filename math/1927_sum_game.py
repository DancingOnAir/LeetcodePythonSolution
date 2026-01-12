from math import ceil


class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        left_sum, right_sum, left_wildcard, right_wildcard = 0, 0, 0, 0
        for i in range(n):
            if i < n // 2:
                if num[i] == '?':
                    left_wildcard += 1
                else:
                    left_sum += int(num[i])
            else:
                if num[i] == '?':
                    right_wildcard += 1
                else:
                    right_sum += int(num[i])

        return not ((left_sum + left_wildcard / 2 * 9) == (right_sum + right_wildcard / 2 * 9))


def test_sum_game():
    solution = Solution()
    assert not solution.sumGame("5023"), 'wrong result'
    assert solution.sumGame("25??"), 'wrong result'
    assert not solution.sumGame("?3295???"), 'wrong result'


if __name__ == '__main__':
    test_sum_game()
