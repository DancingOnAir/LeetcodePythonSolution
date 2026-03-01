from typing import List
from collections import defaultdict


class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        seen = defaultdict(int)
        for w in words:
            if len(w) >= k:
                seen[w[:k]] += 1
        return sum(1 for v in seen.values() if v > 1)


def test_prefix_connected():
    solution = Solution()
    assert solution.prefixConnected(["pljhjnzwwufsnubivzbnhj","pjbkpctukizinffgworaug","psskreusinrefcbwbzcbwrtjxmaertjaodhxkbfpmshojzuinqfwggeixhxunshwkplhhnwczjcmyrljnzgvmagumdiamqj","prgscabbwglfepqlbxevnvjrqlgvcnmtkhzbhqrxfdyjdiejhrarnlytligceylvgspnrsltqfqskphvrtnmvguljdrlguwsf"], 1) == 1, 'wrong result'
    assert solution.prefixConnected(["apple", "apply", "banana", "bandit"], 2) == 2, 'wrong result'
    assert solution.prefixConnected(["car", "cat", "cartoon"], 3) == 1, 'wrong result'
    assert solution.prefixConnected(["bat", "dog", "dog", "doggy", "bat"], 3) == 2, 'wrong result'


if __name__ == '__main__':
    test_prefix_connected()
