from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(int(d[-4:-2]) > 60 for d in details)


def test_count_seniors():
    solution = Solution()
    assert solution.countSeniors(["7868190130M7522", "5303914400F9211", "9273338290F4010"]) == 2, 'wrong result'
    assert solution.countSeniors(["1313579440F2036", "2921522980M5644"]) == 0, 'wrong result'


if __name__ == '__main__':
    test_count_seniors()
