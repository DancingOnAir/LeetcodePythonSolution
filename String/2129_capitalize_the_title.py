class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return ' '.join(w.capitalize() if len(w) > 2 else w.lower() for w in title.split())


def test_capitalize_title():
    solution = Solution()
    assert solution.capitalizeTitle("capiTalIze tHe titLe") == "Capitalize The Title", 'wrong result'
    assert solution.capitalizeTitle("First leTTeR of EACH Word") == "First Letter of Each Word", 'wrong result'
    assert solution.capitalizeTitle("i lOve leetcode") == "i Love Leetcode", 'wrong result'


if __name__ == '__main__':
    test_capitalize_title()
