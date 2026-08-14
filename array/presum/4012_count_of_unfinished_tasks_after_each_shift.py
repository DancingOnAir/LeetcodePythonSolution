from bisect import bisect_right


class Solution:
    def countTasks(self, tasks: list[int], shifts: list[int]) -> list[int]:
        m = len(tasks)
        acc = [0] * (m + 1)
        for i, x in enumerate(tasks):
            acc[i + 1] = acc[i] + x

        res = []
        remaining = 0
        for i, x in enumerate(shifts):
            j = bisect_right(acc, remaining + x)
            res.append(m - j + 1)
            remaining += x
            if remaining >= acc[-1]:
                remaining = 0
        return res


def test_count_tasks():
    solution = Solution()
    assert solution.countTasks([1, 4, 4], shifts=[9, 1, 4]) == [0, 2, 1], 'wrong result'
    assert solution.countTasks([2, 3, 4], shifts=[20, 4, 5]) == [0, 2, 0], 'wrong result'
    assert solution.countTasks([4, 2], shifts=[3, 6, 1]) == [2, 0, 2], 'wrong result'


if __name__ == '__main__':
    test_count_tasks()
