class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count('1')
        ss = [x for x in s.split('1') if x]
        if len(ss) < 2:
            return ones
        zeros = 0
        for i in range(len(ss) - 1):
            cur = len(ss[i]) + len(ss[i + 1])
            zeros = max(zeros, cur)
        return ones + zeros

    def maxActiveSectionsAfterTrade1(self, s: str) -> int:
        active = 0
        current_inactive = 0
        last_inactive = 0
        mx = 0
        for c in s:
            if c == '0':
                current_inactive += 1
            else:
                active += 1
                if current_inactive > 0:
                    if last_inactive > 0:
                        mx = max(mx, current_inactive + last_inactive)
                    last_inactive = current_inactive
                current_inactive = 0
        if current_inactive > 0 and last_inactive > 0:
            mx = max(mx, current_inactive + last_inactive)
        return active + mx


def test_max_active_sections_after_trade():
    solution = Solution()
    assert solution.maxActiveSectionsAfterTrade("01") == 1, 'wrong result'
    assert solution.maxActiveSectionsAfterTrade("0100") == 4, 'wrong result'
    assert solution.maxActiveSectionsAfterTrade("1000100") == 7, 'wrong result'
    assert solution.maxActiveSectionsAfterTrade("01010") == 4, 'wrong result'


if __name__ == '__main__':
    test_max_active_sections_after_trade()
