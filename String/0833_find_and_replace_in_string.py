from typing import List


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        for i, source, target in sorted(zip(indices, sources, targets), reverse=True):
            s = s[:i] + target + s[i+len(source):] if s[i: i+len(source)] == source else s
        return s

    def findReplaceString1(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        indices = sorted((v, i) for i, v in enumerate(indices))
        indices.append((len(s), len(indices)))
        res = []
        i, j = 0, 0
        while i < len(s):
            cur = indices[j]
            if i == cur[0]:
                if s[i: i+len(sources[cur[1]])] == sources[cur[1]]:
                    res.append(targets[cur[1]])
                    i += len(sources[cur[1]])
                    j += 1
                else:
                    j += 1
                    res.append(s[i: indices[j][0]])
                    i = indices[j][0]
            else:
                res.append(s[i])
                i += 1
        return ''.join(res)


def test_find_replace_string():
    solution = Solution()
    assert solution.findReplaceString("mhnbzxkwzxtaanmhtoirxheyanoplbvjrovzudznmetkkxrdmr", [46,29,2,44,31,26,42,9,38,23,36,12,16,7,33,18], ["rym","kv","nbzxu","vx","js","tp","tc","jta","zqm","ya","uz","avm","tz","wn","yv","ird"], ["gfhc","uq","dntkw","wql","s","dmp","jqi","fp","hs","aqz","ix","jag","n","l","y","zww"]) == "mhnbzxkwzxtaanmhtoirxheaqznoplbvjrovzudznmetkkxrdmr", 'wrong result'
    # assert solution.findReplaceString("vmokgggqzp", [3, 5, 1], ["kg","ggq","mo"], ["s","so","bfr"]) == "eeebffff", 'wrong result'
    assert solution.findReplaceString("abcd", [0, 2], ["a", "cd"], ["eee", "ffff"]) == "eeebffff", 'wrong result'
    assert solution.findReplaceString("abcd", [0, 2], ["ab", "ec"], ["eee", "ffff"]) == "eeecd", 'wrong result'


if __name__ == '__main__':
    test_find_replace_string()
