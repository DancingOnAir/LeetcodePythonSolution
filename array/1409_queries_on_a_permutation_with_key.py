from typing import List
from sortedcontainers import SortedList


class Fenwick:
    def __init__(self, n):
        sz = 1
        while sz <= n:
            sz *= 2
        self.size = sz
        self.data = [0] * sz

    def sum(self, i):
        res = 0
        while i > 0:
            res += self.data[i]
            i -= i & (-i)
        return res

    def update(self, i, val):
        while i < self.size:
            self.data[i] += val
            i += i & (-i)


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        fenwick = Fenwick(2 * m)
        vimap = {}
        for i in range(1, m + 1):
            fenwick.update(i + m, 1)
            vimap[i] = i + m
        cur = m

        res = []
        for q in queries:
            i = vimap.pop(q)
            rank = fenwick.sum(i - 1)
            res.append(rank)

            vimap[q] = cur
            fenwick.update(i, -1)
            fenwick.update(cur, 1)
            cur -= 1

        return res

    # sorted list
    def processQueries3(self, queries: List[int], m: int) -> List[int]:
        vpos = {i+1: i for i in range(m)}
        poses = SortedList(range(m))

        res = []
        front = -1
        for v in queries:
            pos = vpos[v]
            res.append(poses.index(pos))

            vpos[v] = front
            poses.remove(pos)
            poses.add(front)
            front -= 1

        return res

    # insert
    def processQueries2(self, queries: List[int], m: int) -> List[int]:
        res = []
        z = [i for i in range(1, m + 1)]

        for val in queries:
            i = z.index(val)
            res.append(i)

            z.insert(0, z.pop(i))

        return res

    def processQueries1(self, queries: List[int], m: int) -> List[int]:
        res = []
        for i, val in enumerate(queries):
            pos = val - 1
            greater = []
            move_flag = False
            for num in queries[:i]:
                if not move_flag:
                    if num > val and num not in greater:
                        pos += 1
                        greater.append(num)
                    elif num == val:
                        pos = 0
                        move_flag = True
                        greater = []
                elif num == val:
                    pos = 0
                    greater = []
                else:
                    if num not in greater:
                        pos += 1
                        greater.append(num)

            res.append(pos)
        return res


def test_process_queries():
    solution = Solution()

    # queries1 = [3, 1, 2, 1]
    # m1 = 5
    # print(solution.processQueries(queries1, m1))
    #
    # queries2 = [4, 1, 2, 2]
    # m2 = 4
    # print(solution.processQueries(queries2, m2))
    #
    # queries3 = [7, 5, 5, 8, 3]
    # m3 = 8
    # print(solution.processQueries(queries3, m3))

    queries4 = [8, 7, 4, 2, 8, 1, 7, 7]
    m4 = 8
    print(solution.processQueries(queries4, m4))

    queries5 = [10, 7, 3, 3, 9, 4, 1, 4, 9, 9]
    m5 = 10
    print(solution.processQueries(queries5, m5))


if __name__ == '__main__':
    test_process_queries()
