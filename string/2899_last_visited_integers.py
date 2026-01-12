from typing import List


class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        res, nums = [], []
        cnt = 0

        for w in words:
            if w == "prev":
               cnt -= 1
               res.append(nums[cnt] if -cnt <= len(nums) else -1)
            else:
                nums.append(int(w))
                cnt = 0
        return res


def test_last_visited_integers():
    solution = Solution()
    assert solution.lastVisitedIntegers(["1", "2", "prev", "prev", "prev"]) == [2, 1, -1], 'wrong result'
    assert solution.lastVisitedIntegers(["1", "prev", "2", "prev", "prev"]) == [1, 2, 1], 'wrong result'


if __name__ == '__main__':
    test_last_visited_integers()

