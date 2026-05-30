class Solution:
    def passwordStrength(self, password: str) -> int:
        s = set(password)
        res = 0
        for c in s:
            if c.islower():
                res += 1
            elif c.isupper():
                res += 2
            elif c.isdigit():
                res += 3
            else:
                res += 5
        return res


def test_password_strength():
    solution = Solution()
    assert solution.passwordStrength("vqztn2Z") == 10, 'wrong result'
    assert solution.passwordStrength("aA1!") == 11, 'wrong result'
    assert solution.passwordStrength("bbB11#") == 11, 'wrong result'


if __name__ == '__main__':
    test_password_strength()
