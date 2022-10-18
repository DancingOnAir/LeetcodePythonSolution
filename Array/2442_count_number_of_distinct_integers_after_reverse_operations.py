from typing import List


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        nums.extend([int(x) for x in str(nums)[-2:0:-1].split(',')])
        return len(set(nums))

    def countDistinctIntegers2(self, nums: List[int]) -> int:
        return len({b for a in nums for b in (a, int(str(a)[::-1]))})

    def countDistinctIntegers1(self, nums: List[int]) -> int:
        return len({int(str(x)[::-1]) for x in nums} | set(nums))


def test_count_distinct_integers():
    solution = Solution()
    assert solution.countDistinctIntegers([1, 13, 10, 12, 31]) == 6, 'wrong result'
    assert solution.countDistinctIntegers([2, 2, 2]) == 1, 'wrong result'


if __name__ == '__main__':
    test_count_distinct_integers()
