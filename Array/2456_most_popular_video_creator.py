from typing import List
from collections import defaultdict


class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        tot, vis, mx = defaultdict(int), defaultdict(list), 0
        for c, i, v in zip(creators, ids, views):
            tot[c] += v
            vis[c].append((-v, i))
            mx = max(mx, tot[c])

        return [[c, min(v)[1]] for c, v in vis.items() if tot[c] == mx]

    def mostPopularCreator1(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        m = dict()
        for i in range(len(creators)):
            if creators[i] not in m:
                m[creators[i]] = [i, views[i]]
            else:
                if views[i] > views[m[creators[i]][0]] or (views[i] == views[m[creators[i]][0]] and ids[i] < ids[m[creators[i]][0]]):
                    m[creators[i]][0] = i
                m[creators[i]][1] += views[i]

        res = list()
        mx = max(m.values(), key=lambda x: x[1])
        for k, v in m.items():
            if v[1] == mx[1]:
                res.append([k, ids[v[0]]])
        return res


def test_most_popular_creator():
    solution = Solution()
    assert solution.mostPopularCreator(["alice", "bob", "alice", "chris"], ["one", "two", "three", "four"], [5, 10, 5, 4]) == [["alice", "one"], ["bob", "two"]], 'wrong result'
    assert solution.mostPopularCreator(["alice", "alice", "alice"], ["a", "b", "c"], [1, 2, 2]) == [["alice", "b"]], 'wrong result'


if __name__ == '__main__':
    test_most_popular_creator()

