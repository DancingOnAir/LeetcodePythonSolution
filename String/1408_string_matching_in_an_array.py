from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        s = ','.join(words)
        return [w for w in words if s.count(w) != 1]

    def stringMatching2(self, words: List[str]) -> List[str]:
        res = list()
        sentence = ','.join(words)
        for s in words:
            if sentence.count(s) != 1:
                res.append(s)
        return res

    def stringMatching1(self, words: List[str]) -> List[str]:
        res = list()

        words.sort(key=len)
        for i, s1 in enumerate(words):
            for s2 in words[i+1:]:
                if s1 in s2:
                    res.append(s1)
                    break
        return res


def test_string_matching():
    solution = Solution()
    assert solution.stringMatching(["mass", "as", "hero", "superhero"]) == ["as", "hero"], 'wrong result'
    assert solution.stringMatching(["leetcode", "et", "code"]) == ["et", "code"], 'wrong result'
    assert solution.stringMatching(["blue", "green", "bu"]) == [], 'wrong result'


if __name__ == '__main__':
    test_string_matching()
