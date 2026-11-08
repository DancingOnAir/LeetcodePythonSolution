from heapq import heappush, heappop, heapify


class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        res = []
        idle = [(w, i) for i, w in enumerate(servers)]
        heapify(idle)

        busy = []
        now = 0

        def release() -> None:
            while busy and busy[0][0] <= now:
                _, i = heappop(busy)
                heappush(idle, (servers[i], i))

        for i, t in enumerate(tasks):
            now = max(now, i)
            release()
            if not idle:
                now = busy[0][0]
                release()
            _, j = heappop(idle)
            heappush(busy, (now + t, j))
            res.append(j)

        return res


def test_assign_tasks():
    solution = Solution()
    assert solution.assignTasks([3, 3, 2], tasks=[1, 2, 3, 2, 1, 2]) == [2, 2, 0, 2, 1, 2], 'wrong result'
    assert solution.assignTasks([5, 1, 4, 3, 2], tasks=[2, 1, 2, 4, 5, 2, 1]) == [1, 4, 1, 4, 1, 3, 2], 'wrong result'


if __name__ == '__main__':
    test_assign_tasks()
