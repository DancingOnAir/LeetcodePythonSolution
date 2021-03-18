class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        count = 0
        a, b = '', ''
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
                if count == 1:
                    a, b = s1[i], s2[i]
                elif count == 2:
                    if a != s2[i] or b != s1[i]:
                        return False

        return count == 2


def test_are_almost_equal():
    solution = Solution()
    assert solution.areAlmostEqual('bank', 'kanb'), 'wrong result'
    assert not solution.areAlmostEqual('attack', 'defend'), 'wrong result'
    assert solution.areAlmostEqual('kelb', 'kelb'), 'wrong result'
    assert not solution.areAlmostEqual('abcd', 'dcba'), 'wrong result'


if __name__ == '__main__':
    test_are_almost_equal()
