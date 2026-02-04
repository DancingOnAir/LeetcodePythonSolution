class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        res = ""
        left = cnt = 0
        for right, ch in enumerate(s):
            if ch == '1':
                cnt += 1

            while cnt == k:
                if not res or len(res) > right - left + 1:
                    res = s[left:right+1]
                elif len(res) == right - left + 1:
                    res = min(res, s[left:right+1])
                if s[left] == '1':
                    cnt -= 1
                left += 1

        return res

    def shortestBeautifulSubstring1(self, s: str, k: int) -> str:
        res = []
        left, cnt = 0, 0

        for right, c in enumerate(s):
            if c == '1':
                cnt += 1

            while cnt == k:
                res.append(s[left: right+1])
                if s[left] == '1':
                    cnt -= 1
                left += 1

        res.sort(key=lambda x: (len(x), x))
        return "" if not res else res[0]


def test_shortest_beautiful_substring():
    solution = Solution()
    assert solution.shortestBeautifulSubstring("100011001", 3) == "11001", 'wrong result'
    assert solution.shortestBeautifulSubstring("1011", 2) == "11", 'wrong result'
    assert solution.shortestBeautifulSubstring("000", 1) == "", 'wrong result'


if __name__ == '__main__':
    test_shortest_beautiful_substring()
