from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = defaultdict(list)
        for word in strs:
            s = ''.join(sorted(word))
            a[s].append(word)
        res = list(a.values())
        return res