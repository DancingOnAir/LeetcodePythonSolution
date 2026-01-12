class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        seen = set()
        for i, ch in enumerate(password):
            if i > 0 and ch == password[i - 1]:
                return False
            if ch.islower():
                seen.add(1)
            elif ch.isupper():
                seen.add(2)
            elif ch.isdigit():
                seen.add(3)
            elif ch in set("!@#$%^&*()-+"):
                seen.add(4)

        return len(password) >= 8 and len(seen) == 4

    def strongPasswordCheckerII1(self, password: str) -> bool:
        if len(password) < 8:
            return False

        pre = ''
        # flag[i] = 1 means existing of lowercase, uppercase, digit and special char
        flag = [0] * 4
        for c in password:
            if c == pre:
                return False

            if 97 <= ord(c) <= 122:
                flag[0] = 1
            elif 65 <= ord(c) <= 90:
                flag[1] = 1
            elif c.isdigit():
                flag[2] = 1
            elif c in set("!@#$%^&*()-+"):
                flag[3] = 1

            pre = c

        return sum(flag) == 4


def test_strong_password_checker_ii():
    solution = Solution()
    assert solution.strongPasswordCheckerII("IloveLe3tcode!"), 'wrong result'
    assert not solution.strongPasswordCheckerII("Me+You--IsMyDream"), 'wrong result'
    assert not solution.strongPasswordCheckerII("1aB!"), 'wrong result'


if __name__ == '__main__':
    test_strong_password_checker_ii()
