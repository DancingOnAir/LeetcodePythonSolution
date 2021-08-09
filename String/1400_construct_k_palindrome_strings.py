from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        cnt = Counter(s)
        odd = sum(1 if val & 1 else 0 for val in cnt.values())

        mx = len(s)
        mi = odd
        return mi <= k <= mx


def test_can_construct():
    solution = Solution()

    assert solution.canConstruct("annabelle", 1), 'wrong result'
    assert not solution.canConstruct("cxayrgpcctwlfupgzirmazszgfiusitvzsnngmivctprcotcuutfxdpbrdlqukhxkrmpwqqwdxxrptaftpnilfzcmknqljgbfkzuhksxzplpoozablefndimqnffrqfwgaixsovmmilicjwhppikryerkdidupvzdmoejzczkbdpfqkgpbxcrxphhnxfazovxbvaxyxhgqxcxirjsryqxtreptusvupsstylpjniezyfokbowpbgxbtsemzsvqzkbrhkvzyogkuztgfmrprz", 5), 'wrong result'
    assert solution.canConstruct("qlkzenwmmnpkopu", 15), 'wrong result'
    assert solution.canConstruct("aaa", 2), 'wrong result'
    assert solution.canConstruct("annabelle", 2), 'wrong result'
    assert not solution.canConstruct("leetcode", 3), 'wrong result'
    assert solution.canConstruct("true", 4), 'wrong result'
    assert solution.canConstruct("yzyzyzyzyzyzyzy", 2), 'wrong result'
    assert not solution.canConstruct("cr", 7), 'wrong result'


if __name__ == '__main__':
    test_can_construct()
