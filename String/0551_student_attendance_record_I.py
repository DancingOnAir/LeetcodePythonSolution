class Solution:
    def checkRecord(self, s: str) -> bool:
        cnt_A = cnt_L = 0
        for c in s:
            if c == 'A':
                cnt_A += 1
                if cnt_A > 1:
                    return False
                cnt_L = 0
            elif c == 'L':
                cnt_L += 1
                if cnt_L > 2:
                    return False
            else:
                cnt_L = 0
        return True

    def checkRecord1(self, s: str) -> bool:
        return s.count('A') < 2 and 'LLL' not in s


def test_check_record():
    solution = Solution()
    assert solution.checkRecord('PPALLP'), 'wrong result'
    assert not solution.checkRecord('PPALLL'), 'wrong result'


if __name__ == '__main__':
    test_check_record()
