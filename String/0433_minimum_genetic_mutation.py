from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
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
                            seen.remove(cur)

        bfs(startGene, 0)
        return res


def test_min_mutation():
    solution = Solution()
    assert solution.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]) == 1, 'wrong result'
    assert solution.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"]) == 2, 'wrong result'


if __name__ == '__main__':
    test_min_mutation()
