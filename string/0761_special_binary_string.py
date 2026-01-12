class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if len(s) == 0:
            return s

        specials = []
        j, tot = 0, 0
        for i in range(len(s)):
            tot += (1 if s[i] == '1' else -1)
            if tot == 0:
                specials.append("1" + self.makeLargestSpecial(s[j + 1: i]) + "0")
                j = i + 1
        return ''.join(sorted(specials)[::-1])


def test_make_largest_special():
    solution = Solution()
    assert solution.makeLargestSpecial("11011000") == "11100100", 'wrong result'
    assert solution.makeLargestSpecial("10") == "10", 'wrong result'


if __name__ == '__main__':
    test_make_largest_special()
