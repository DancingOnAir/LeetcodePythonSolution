from typing import List
from collections import Counter


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        a = [c for c, v in Counter(arr).items() if v == 1]
        return a[k - 1] if len(a) >= k else ''


def test_kth_distinct():
    solution = Solution()

    assert solution.kthDistinct(["d", "b", "c", "b", "c", "a"], 2) == "a", 'wrong result'
    assert solution.kthDistinct(["aaa", "aa", "a"], 1) == "aaa", 'wrong result'
    assert solution.kthDistinct(["a", "b", "a"], 3) == "", 'wrong result'


if __name__ == '__main__':
    test_kth_distinct()
