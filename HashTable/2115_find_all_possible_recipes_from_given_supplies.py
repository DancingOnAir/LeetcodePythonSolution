from typing import List
from collections import defaultdict, deque


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        # DAG: ingredients -> recipes
        graph = defaultdict(list)
        # default in-degree is 0
        in_degree = defaultdict(int)

        # init graph and in-degree
        for i in range(n):
            for ingredient in ingredients[i]:
                in_degree[recipes[i]] += 1
                graph[ingredient].append(recipes[i])

        q = deque(supplies)
        while q:
            cur = q.popleft()
            for nei in graph[cur]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)

        res = list()
        # for all recipes, it would have in-degree of 0
        # so that it can be cooked
        for r in recipes:
            if in_degree[r] == 0:
                res.append(r)
        return res


def test_find_all_recipes():
    solution = Solution()

    assert sorted(solution.findAllRecipes(
        ["xevvq", "izcad", "p", "we", "bxgnm", "vpio", "i", "hjvu", "igi", "anp", "tokfq", "z", "kwdmb", "g", "qb", "q", "b", "hthy"],
        [["wbjr"],
         ["otr", "fzr", "g"],
         ["fzr", "wi", "otr", "xgp", "wbjr", "igi", "b"],
         ["fzr", "xgp", "wi", "otr", "tokfq", "izcad", "igi", "xevvq", "i", "anp"],
         ["wi", "xgp", "wbjr"],
         ["wbjr", "bxgnm", "i", "b", "hjvu", "izcad", "igi", "z", "g"],
         ["xgp", "otr", "wbjr"],
         ["wbjr", "otr"],
         ["wbjr", "otr", "fzr", "wi", "xgp", "hjvu", "tokfq", "z", "kwdmb"],
         ["xgp", "wi", "wbjr", "bxgnm", "izcad", "p", "xevvq"],
         ["bxgnm"],
         ["wi", "fzr", "otr", "wbjr"],
         ["wbjr", "wi", "fzr", "xgp", "otr", "g", "b", "p"],
         ["otr", "fzr", "xgp", "wbjr"],
         ["xgp", "wbjr", "q", "vpio", "tokfq", "we"],
         ["wbjr", "wi", "xgp", "we"],
         ["wbjr"],
         ["wi"]],
        ["wi", "otr", "wbjr", "fzr", "xgp"])) == sorted(["xevvq", "izcad", "bxgnm", "i", "hjvu", "tokfq", "z", "g", "b", "hthy"]), 'wrong result'
    assert sorted(solution.findAllRecipes(["bread"], [["yeast", "flour"]], ["yeast", "flour", "corn"])) == [
        "bread"], 'wrong result'
    assert sorted(solution.findAllRecipes(["bread", "sandwich"], [["yeast", "flour"], ["bread", "meat"]],
                                   ["yeast", "flour", "meat"])) == sorted(["bread", "sandwich"]), 'wrong result'
    assert sorted(solution.findAllRecipes(["bread", "sandwich", "burger"],
                                   [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]],
                                   ["yeast", "flour", "meat"])) == sorted(["bread", "sandwich", "burger"]), 'wrong result'


if __name__ == '__main__':
    test_find_all_recipes()
