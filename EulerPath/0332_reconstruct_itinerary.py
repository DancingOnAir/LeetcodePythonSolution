from typing import List
from collections import defaultdict


class Solution:
    # iterative
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        g = defaultdict(list)
        for u, v in tickets:
            g[u].append(v)
        for k in g:
            g[k].sort(reverse=True)

        res = list()
        stk = ['JFK']
        while stk:
            while g[stk[-1]]:
                stk.append(g[stk[-1]].pop())
            res.append(stk.pop())
        return res[::-1]

    # recursive
    def findItinerary1(self, tickets: List[List[str]]) -> List[str]:
        res = list()
        g = defaultdict(list)
        for u, v in tickets:
            g[u].append(v)
        for k in g:
            g[k].sort(reverse=True)

        def dfs(u):
            while g[u]:
                dfs(g[u].pop())
            res.append(u)

        dfs('JFK')
        return res[::-1]


def test_find_itinerary():
    solution = Solution()
    assert solution.findItinerary([["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]) == ["JFK","ANU","EZE","AXA","TIA","ANU","JFK","TIA","ANU","TIA","JFK"], 'wrong result'
    assert solution.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]) == ["JFK", "MUC", "LHR", "SFO", "SJC"], 'wrong result'
    assert solution.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]) == ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"], 'wrong result'


if __name__ == '__main__':
    test_find_itinerary()
