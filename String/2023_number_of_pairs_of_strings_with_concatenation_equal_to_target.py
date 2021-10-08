from typing import List


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        res = 0
        n = len(nums)

        for i, c1 in enumerate(nums):
            for j, c2 in enumerate(nums):
                if i != j and c1 + c2 == target:
                    res += 1
        return res


def test_num_of_pairs():
    solution = Solution()

    assert solution.numOfPairs(["777", "7", "77", "77"], "7777") == 4, 'wrong result'
    assert solution.numOfPairs(["123", "4", "12", "34"], "1234") == 2, 'wrong result'
    assert solution.numOfPairs(["1", "1", "1"], "11") == 6, 'wrong result'


if __name__ == '__main__':
    test_num_of_pairs()
