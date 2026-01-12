from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank, seen, q = set(bank), {startGene}, [(startGene, 0)]
        for g, step in q:
            for s in (g[:i] + cc + g[i+1:] for i, c in enumerate(g) for cc in "ACGT"):
                if s in bank and s not in seen:
                    if s == endGene:
                        return step + 1

                    seen.add(s)
                    q.append((s, step + 1))
        return -1

    def minMutation1(self, startGene: str, endGene: str, bank: List[str]) -> int:
        res = len(startGene) * 3
        bank = set(bank)
        seen = set()

        def bfs(gene, step):
            if gene == endGene:
                nonlocal res
                res = min(res, step)
                return

            for i, ch in enumerate(gene):
                for x in "ACGT":
                    if ch != x:
                        cur = gene[:i] + x + gene[i+1:]
                        if cur in bank and cur not in seen:
                            seen.add(cur)
                            bfs(cur, step + 1)

        bfs(startGene, 0)
        return res


def test_min_mutation():
    solution = Solution()
    assert solution.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]) == 1, 'wrong result'
    assert solution.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"]) == 2, 'wrong result'


if __name__ == '__main__':
    test_min_mutation()
