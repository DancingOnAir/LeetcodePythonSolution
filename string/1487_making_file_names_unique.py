from typing import List
from collections import defaultdict


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        memo = dict()

        for name in names:
            modified = name
            if name in memo:
                k = memo[name]
                while modified in memo:
                    k += 1
                    modified = f'{name}({k})'
                memo[name] = k
            memo[modified] = 0

        return list(memo.keys())

    def getFolderNames2(self, names: List[str]) -> List[str]:
        res = list()
        memo = set()
        last = defaultdict(int)

        for name in names:
            v = last[name]
            modified = name
            while modified in memo:
                v += 1
                modified = f'{name}({v})'

            last[name] = v
            memo.add(modified)
            res.append(modified)

        return res

    # brute force but TLE
    def getFolderNames1(self, names: List[str]) -> List[str]:
        res = list()
        memo = set()

        for name in names:
            tmp_name = name
            idx = 0
            while tmp_name in memo:
                idx += 1
                tmp_name = '{0}({1})'.format(name, str(idx))
            res.append(tmp_name)
            memo.add(tmp_name)
        return res


def test_get_folder_names():
    solution = Solution()
    # assert solution.getFolderNames(["pes", "fifa", "gta", "pes(2019)"]) == \
    #        ["pes", "fifa", "gta", "pes(2019)"], 'wrong result'
    assert solution.getFolderNames(["gta", "gta(1)", "gta", "avalon"]) == \
           ["gta", "gta(1)", "gta(2)", "avalon"], 'wrong result'
    assert solution.getFolderNames(["onepiece", "onepiece(1)", "onepiece(2)", "onepiece(3)", "onepiece"]) == \
           ["onepiece", "onepiece(1)", "onepiece(2)", "onepiece(3)", "onepiece(4)"], 'wrong result'
    assert solution.getFolderNames(["wano", "wano", "wano", "wano"]) == \
           ["wano", "wano(1)", "wano(2)", "wano(3)"], 'wrong result'
    assert solution.getFolderNames(["kaido", "kaido(1)", "kaido", "kaido(1)"]) == \
           ["kaido", "kaido(1)", "kaido(2)", "kaido(1)(1)"], 'wrong result'
    assert solution.getFolderNames(["kaido", "kaido(1)", "kaido", "kaido(1)", "kaido(2)"]) == \
           ["kaido", "kaido(1)", "kaido(2)", "kaido(1)(1)", "kaido(2)(1)"], 'wrong result'


if __name__ == '__main__':
    test_get_folder_names()
