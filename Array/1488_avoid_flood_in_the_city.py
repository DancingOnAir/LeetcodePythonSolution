from typing import List
from collections import defaultdict
from bisect import bisect_left
import heapq


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        dd = defaultdict(list)
        for i, val in enumerate(rains):
            dd[val].append(i)

        res = [-1] * len(rains)
        full = set()
        closest = []
        for i, lake in enumerate(rains):
            if not lake:
                if closest:
                    res[i] = rains[heapq.heappop(closest)]
                    full.remove(res[i])
                else:
                    res[i] = 1
            else:
                if lake in full:
                    return []

                full.add(lake)
                dd[lake].pop(0)
                if dd[lake]:
                    heapq.heappush(closest, dd[lake][0])

        return res

    def avoidFlood1(self, rains: List[int]) -> List[int]:
        res = []
        dd = defaultdict(list)

        for i, val in enumerate(rains):
            if val:
                if not len(dd[val]):
                    res.append(-1)
                else:
                    if not len(dd[0]):
                        return []
                    else:
                        if dd[0][-1] < dd[val][0]:
                            return []

                        pos = bisect_left(dd[0], dd[val].pop())
                        res[dd[0][pos]] = val
                        dd[0].pop(pos)
                        res.append(-1)
            else:
                res.append(1)
            dd[val] += [i]

        return res


def test_avoid_flood():
    solution = Solution()

    rains1 = [1, 2, 3, 4]
    print(solution.avoidFlood(rains1))

    rains2 = [1, 2, 0, 0, 2, 1]
    print(solution.avoidFlood(rains2))

    rains3 = [1, 2, 0, 1, 2]
    print(solution.avoidFlood(rains3))

    rains4 = [69, 0, 0, 0, 69]
    print(solution.avoidFlood(rains4))

    rains5 = [10, 20, 20]
    print(solution.avoidFlood(rains5))

    rains6 = [2, 3, 0, 0, 3, 1, 0, 1, 0, 2, 2]
    print(solution.avoidFlood(rains6))

    rains7 = [1, 0, 2, 0, 2, 1]
    print(solution.avoidFlood(rains7))


if __name__ == '__main__':
    test_avoid_flood()
