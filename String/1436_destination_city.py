from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starts, dests = map(set, zip(*paths))
        return (dests - starts).pop()

    def destCity1(self, paths: List[List[str]]) -> str:
        res = ''
        memo = dict()
        for p in paths:
            memo[p[0]] = p[1]
            if not res:
                res = p[1]
            while res in memo:
                res = memo[res]
        return res


def test_dest_city():
    solution = Solution()
    assert solution.destCity(
        [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]) == "Sao Paulo", 'wrong result'
    assert solution.destCity([["B", "C"], ["D", "B"], ["C", "A"]]) == "A", 'wrong result'
    assert solution.destCity([["A", "Z"]]) == "Z", 'wrong result'
    assert solution.destCity([["qMTSlfgZlC", "ePvzZaqLXj"], ["xKhZXfuBeC", "TtnllZpKKg"], ["ePvzZaqLXj", "sxrvXFcqgG"],
                              ["sxrvXFcqgG", "xKhZXfuBeC"],
                              ["TtnllZpKKg", "OAxMijOZgW"]]) == "OAxMijOZgW", 'wrong result'


if __name__ == '__main__':
    test_dest_city()
