class Solution:
    def maskPII(self, s: str) -> str:
        at = s.find('@')
        if at >= 0:
            return (s[0] + '*' * 5 + s[at - 1:]).lower()
        s = ''.join(c for c in s if c.isdigit())
        return ["", "+*-", "+**-", "+***-"][len(s) - 10] + "***-***-" + s[-4:]

    # brute force
    def maskPII1(self, s: str) -> str:
        i = 0
        flag = 1
        if s[i].isalpha():
            flag = 0

        res = ''
        while i < len(s):
            if flag == 0:
                if i == 0:
                    res += s[i].lower()
                    res += "*" * 5
                elif s[i] == '@':
                    res += s[i - 1].lower()
                    res += s[i:].lower()
                    break
            else:
                if s[i].isdigit():
                    res += s[i]
            i += 1

        if flag == 1:
            cnt = len(res) - 10
            pre = ""
            if cnt > 0:
                pre = '*' * cnt + '-'
            res = pre + "***-***-" + res[-4:]
        return res


def test_mask_pii():
    solution = Solution()
    assert solution.maskPII("LeetCode@LeetCode.com") == "l*****e@leetcode.com", 'wrong result'
    assert solution.maskPII("AB@qq.com") == "a*****b@qq.com", 'wrong result'
    assert solution.maskPII("1(234)567-890") == "***-***-7890", 'wrong result'


if __name__ == '__main__':
    test_mask_pii()
