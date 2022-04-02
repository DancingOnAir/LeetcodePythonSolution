class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.count('A') < 2 and 'LLL' not in s


def test_check_record():
    solution = Solution()
    assert solution.checkRecord('PPALLP'), 'wrong result'
    assert not solution.checkRecord('PPALLL'), 'wrong result'


if __name__ == '__main__':
    test_check_record()
