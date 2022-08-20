from typing import List
from collections import Counter


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        return sorted((Counter(dict(items1)) + Counter(dict(items2))).items())

    def mergeSimilarItems1(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        c = Counter()
        for v, w in items1 + items2:
            c[v] += w
        return sorted(c.items())


def test_merge_similar_items():
    solution = Solution()
    assert solution.mergeSimilarItems([[1, 1], [4, 5], [3, 8]], [[3, 1], [1, 5]]) == [[1, 6], [3, 9], [4, 5]], 'wrong result'
    assert solution.mergeSimilarItems([[1, 1], [3, 2], [2, 3]], [[2, 1], [3, 2], [1, 3]]) == [[1, 4], [2, 4], [3, 4]], 'wrong result'


if __name__ == '__main__':
    test_merge_similar_items()
