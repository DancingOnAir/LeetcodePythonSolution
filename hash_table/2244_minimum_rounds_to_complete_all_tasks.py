from collections import Counter


class Solution:
    def minimumRounds(self, tasks: list[int]) -> int:
        cnt = Counter(tasks)
        res = 0
        for v in cnt.values():
            if v == 1:
                return -1
            q, r = divmod(v, 3)
            res += q
            if r != 0:
                res += 1
        return res


def test_minimum_rounds():
    solution = Solution()
    assert solution.minimumRounds([2, 2, 3, 3, 2, 4, 4, 4, 4, 4]) == 4, 'wrong result'
    assert solution.minimumRounds([2, 3, 3]) == -1, 'wrong result'


if __name__ == '__main__':
    test_minimum_rounds()
