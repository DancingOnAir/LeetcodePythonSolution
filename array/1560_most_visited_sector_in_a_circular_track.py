from typing import List


class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        return list(range(rounds[0], rounds[-1] + 1)) or list(range(1, rounds[-1] + 1)) + list(range(rounds[0], n + 1))

    def mostVisited1(self, n: int, rounds: List[int]) -> List[int]:
        return [x for x in range(rounds[0], rounds[-1] + 1)] if rounds[0] <= rounds[-1] \
            else [x for x in range(1, rounds[-1] + 1)] + [y for y in range(rounds[0], n + 1)]


def test_most_visited():
    solution = Solution()

    n1 = 4
    rounds1 = [1, 3, 1, 2]
    print(solution.mostVisited(n1, rounds1))
    assert solution.mostVisited(n1, rounds1) == [1, 2], "wrong result"

    n2 = 2
    rounds2 = [2, 1, 2, 1, 2, 1, 2, 1, 2]
    assert solution.mostVisited(n2, rounds2) == [2], "wrong result"

    n3 = 7
    rounds3 = [1, 3, 5, 7]
    assert solution.mostVisited(n3, rounds3) == [1, 2, 3, 4, 5, 6, 7], "wrong result"

    n4 = 3
    rounds4 = [3, 2, 1, 2, 1, 3, 2, 1, 2, 1, 3, 2, 3, 1]
    print(solution.mostVisited(n4, rounds4))
    assert solution.mostVisited(n4, rounds4) == [1, 3], "wrong result"


if __name__ == '__main__':
    test_most_visited()
