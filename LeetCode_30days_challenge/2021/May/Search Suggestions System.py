from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        suggested = []
        n = len(products)
        m = len(searchWord)
        start, end = 0, n - 1
        for i in range(m):
            curr_suggested = []
            good = False
            for j in range(start, end + 1):
                if len(products[j]) < i + 1:
                    if good:
                        end = j - 1
                        break
                    else:
                        start += 1
                    continue
                if searchWord[i] == products[j][i]:
                    good = True
                    curr_suggested.append(products[j])
                    if len(curr_suggested) == 3:
                        break
                else:
                    if good:
                        end = j - 1
                        break
                    else:
                        start += 1
            suggested.append(curr_suggested[:3])
        return suggested
