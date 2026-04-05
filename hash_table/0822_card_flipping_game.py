class Solution:
    def flipgame(self, fronts: list[int], backs: list[int]) -> int:
        m = {a for a, b in zip(fronts, backs) if a == b}
        return min((x for x in fronts + backs if x not in m), default=0)


def test_flip_game():
    solution = Solution()
    assert solution.flipgame([1, 2, 4, 4, 7], backs=[1, 3, 4, 1, 3]) == 2, 'wrong result'
    assert solution.flipgame([1], backs=[1]) == 0, 'wrong result'


if __name__ == '__main__':
    test_flip_game()
