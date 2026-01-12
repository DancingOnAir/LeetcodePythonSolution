from typing import List
from collections import defaultdict


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        m = defaultdict(int)
        for cpd in cpdomains:
            times, domain = cpd.split()
            subdomain = domain.split('.')
            for i in range(len(subdomain)):
                m['.'.join(subdomain[i:])] += int(times)
        return [f"{v} {k}" for k, v in m.items()]


def test_subdomain_visits():
    solution = Solution()
    assert solution.subdomainVisits(["9001 discuss.leetcode.com"]) == ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"], 'wrong result'
    assert solution.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]) == ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"], 'wrong result'


if __name__ == '__main__':
    test_subdomain_visits()
