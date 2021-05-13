class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n == 1:
            return True

        s1 = sorted(s1)
        s2 = sorted(s2)

        if s1 > s2 and any(s1[i] < s2[i] for i in range(n)):
            return False
        elif s2 > s1 and any(s1[i] > s2[i] for i in range(n)):
            return False
        elif s1 == s2:
            return False
        return True


def test_check_if_can_break():
    solution = Solution()
    assert solution.checkIfCanBreak('abc', 'xya'), 'wrong result'
    assert not solution.checkIfCanBreak('abe', 'acd'), 'wrong result'
    assert solution.checkIfCanBreak('leetcodee', 'interview'), 'wrong result'
    
    
if __name__ == '__main__':
    test_check_if_can_break()
