from typing import List
from collections import Counter


class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        return Counter(nums).most_common(1)[0][1] < 3


def test_is_possible_to_split():
    solution = Solution()
    assert solution.isPossibleToSplit([1,1,2,2,3,4]) , 'wrong result'
    assert not solution.isPossibleToSplit([1,1,1,1]) , 'wrong result'


if __name__ == '__main__':
    test_is_possible_to_split()
