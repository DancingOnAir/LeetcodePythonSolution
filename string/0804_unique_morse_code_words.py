from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        return len({''.join(morse[ord(c) - ord('a')] for c in w) for w in words})

    def uniqueMorseRepresentations1(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = set()
        for w in words:
            res.add(''.join(morse[ord(c) - ord('a')] for c in w))
        return len(res)


def test_unique_morse_representations():
    solution = Solution()
    assert solution.uniqueMorseRepresentations(["gin","zen","gig","msg"]) == 2, 'wrong result'
    assert solution.uniqueMorseRepresentations(["a"]) == 1, 'wrong result'


if __name__ == '__main__':
    test_unique_morse_representations()
