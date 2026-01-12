from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = pre = 0
        for s in bank:
            ones = s.count('1')
            if ones > 0:
                res += ones * pre
                pre = ones
        return res


def test_number_of_beams():
    solution = Solution()

    assert solution.numberOfBeams(["011001", "000000", "010100", "001000"]) == 8, 'wrong result'
    assert solution.numberOfBeams(["000", "111", "000"]) == 0, 'wrong result'


if __name__ == '__main__':
    test_number_of_beams()
