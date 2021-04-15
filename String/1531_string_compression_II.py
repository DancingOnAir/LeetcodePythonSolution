from itertools import groupby
from functools import lru_cache


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        # start: start index of string, last: previous char,
        # last_count: num of consecutive previous char, chance: num of left k
        @lru_cache(None)
        def counter(start, last, last_count, chance):
            if chance < 0:
                return float('inf')
            if start == len(s):
                return 0

            if s[start] == last:
                incre = 1 if last_count in [1, 9, 99] else 0
                return incre + counter(start + 1, last, last_count + 1, chance)
            else:
                keep_cur_char = 1 + counter(start + 1, s[start], 1, chance)
                delete_cur_char = counter(start + 1, last, last_count, chance - 1)
                return min(keep_cur_char, delete_cur_char)
        return counter(0, '', 0, k)


def test_get_length_of_optimal_compression():
    solution = Solution()
    assert solution.getLengthOfOptimalCompression('aaabcccd', 2) == 4, 'wrong result'
    assert solution.getLengthOfOptimalCompression('aabbaa', 2) == 2, 'wrong result'
    assert solution.getLengthOfOptimalCompression('aaaaaaaaaaa', 0) == 3, 'wrong result'


if __name__ == '__main__':
    test_get_length_of_optimal_compression()
