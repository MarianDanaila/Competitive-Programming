import collections


class Solution:
    def accountsMerge(self, accounts):
        nr_mails = 0
        for i in range(len(accounts)):
            nr_mails += len(accounts[i]) - 1
        subsets = [[i, 0] for i in range(nr_mails)]

        def find(v):
            if subsets[v][0] != v:
                subsets[v][0] = find(subsets[v][0])
            return subsets[v][0]

        def union(v1, v2):
            if subsets[v1][1] < subsets[v2][1]:
                subsets[v1][0] = v2
            elif subsets[v1][1] > subsets[v2][1]:
                subsets[v2][0] = v1
            else:
                subsets[v1][0] = v2
                subsets[v2][1] += 1

        em_to_id = {}
        em_to_name = {}
        idx = 0
        for acc in accounts:
            name = acc[0]
            first_mail = acc[1]
            for i in range(1, len(acc)):
                mail = acc[i]
                if mail not in em_to_id:
                    em_to_name[mail] = name
                    em_to_id[mail] = idx
                    idx += 1
                set1 = find(em_to_id[first_mail])
                set2 = find(em_to_id[mail])
                if set1 != set2:
                    union(set1, set2)

        ans = collections.defaultdict(list)
        for mail in em_to_id:
            mail_set = find(em_to_id[mail])
            ans[mail_set].append(mail)
        return [[em_to_name[v[0]]] + sorted(v) for v in ans.values()]
