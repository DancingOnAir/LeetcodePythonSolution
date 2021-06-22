from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for e in emails:
            local, domain = e.split('@')
            local = local.split('+')[0].replace('.', '')
            seen.add(local + '@' + domain)
        return len(seen)

    def numUniqueEmails1(self, emails: List[str]) -> int:
        res = list()
        for e in emails:
            at_pos = e.find('@')
            plus_pos = e.find('+')

            if plus_pos != -1:
                local_name = e[:plus_pos]
            else:
                local_name = e[:at_pos]
            local_name = ''.join(local_name.split('.'))
            domain_name = e[at_pos+1:]
            res.append(local_name + '@' + domain_name)
        return len(set(res))


def test_num_unique_emails():
    solution = Solution()

    assert solution.numUniqueEmails(["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com",
                                     "testemail+david@lee.tcode.com"]) == 2, 'wrong result'
    assert solution.numUniqueEmails(["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]) == 3, 'wrong result'


if __name__ == '__main__':
    test_num_unique_emails()


