class Solution:
    def capitalizeTitle(self, title: str) -> str:
        def toggle_capitalize(c):
            return chr(ord(c) ^ 32)

        res = list()
        for w in title.split():
            if len(w) < 3:
                res.append(w.lower())
            else:
                w = list(w.lower())
                w[0] = toggle_capitalize(w[0])
                res.append(''.join(w))
        return ' '.join(res)

    # one line with capitalize and lower
    def capitalizeTitle1(self, title: str) -> str:
        return ' '.join(w.capitalize() if len(w) > 2 else w.lower() for w in title.split())

    def capitalizeTitle2(self, title: str) -> str:
        title = list(title)
        j = 0
        for i in range(len(title) + 1):
            if i == len(title) or title[i] == ' ':
                if i - j > 2:
                    title[j] = title[j].upper()
                j = i + 1
            else:
                title[i] = title[i].lower()
        return ''.join(title)


def test_capitalize_title():
    solution = Solution()
    assert solution.capitalizeTitle("capiTalIze tHe titLe") == "Capitalize The Title", 'wrong result'
    assert solution.capitalizeTitle("First leTTeR of EACH Word") == "First Letter of Each Word", 'wrong result'
    assert solution.capitalizeTitle("i lOve leetcode") == "i Love Leetcode", 'wrong result'


if __name__ == '__main__':
    test_capitalize_title()
