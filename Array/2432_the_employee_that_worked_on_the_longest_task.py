from typing import List


class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        pre, res = 0, (0, 0)
        for idx, cur in logs:
            # 注意这里是pre - cur，得到的是个负数，因为我们要求最大的工作时间，也就是最小的pre - cur的值
            res = min(res, (pre - cur, idx))
            pre = cur
        return res[1]

    def hardestWorker1(self, n: int, logs: List[List[int]]) -> int:
        res = s = 0
        longest_time = 0
        for i, e in logs:
            if e - s > longest_time:
                longest_time = e - s
                res = i
            elif e - s == longest_time and i < res:
                res = i
            s = e

        return res


def test_hardest_worker():
    solution = Solution()
    assert solution.hardestWorker(10, [[0, 3], [2, 5], [0, 9], [1, 15]]) == 1, 'wrong result'
    assert solution.hardestWorker(26, [[1, 1], [3, 7], [2, 12], [7, 17]]) == 3, 'wrong result'
    assert solution.hardestWorker(2, [[0, 10], [1, 20]]) == 0, 'wrong result'


if __name__ == '__main__':
    test_hardest_worker()

