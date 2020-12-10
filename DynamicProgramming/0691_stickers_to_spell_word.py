from typing import List
from collections import defaultdict


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        target_dict = defaultdict(int)
        for c in target:
            target_dict[c] += 1

        print(target_dict)
        pass


def test_min_stickers():
    solution = Solution()

    assert solution.minStickers(["with", "example", "science"], "thehat") == 3, 'wrong result'
    assert solution.minStickers(["notice", "possible"], "basicbasic") == -1, 'wrong result'


if __name__ == '__main__':
    test_min_stickers()
