from typing import List


class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        diff = sorted(a - b for a, b in zip(reward1, reward2))
        return sum(reward2) + sum(diff[-k:])

    def miceAndCheese1(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        diff = [[reward1[i] - reward2[i], i] for i in range(n)]
        s = set()
        for d, i in sorted(diff, reverse=True):
            if k == 0:
                break
            s.add(i)
            k -= 1

        res = 0
        for i in range(n):
            if i in s:
                res += reward1[i]
            else:
                res += reward2[i]
        return res


def test_mice_and_cheese():
    solution = Solution()
    assert solution.miceAndCheese([1, 1, 3, 4], [4, 4, 1, 1], 2) == 15, 'wrong result'
    assert solution.miceAndCheese([1, 1], [1, 1], 2) == 2, 'wrong result'


if __name__ == '__main__':
    test_mice_and_cheese()
