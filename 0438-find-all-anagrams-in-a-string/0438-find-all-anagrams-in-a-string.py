from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        if n < m:
            return []
        
        p_count = Counter(p)
        s_count = Counter()
        result = []
        left = 0
        
        for right in range(n):
            s_count[s[right]] += 1

            if right - left + 1 > m:
                s_count[s[left]] -= 1
                if s_count[s[left]] == 0:
                    del s_count[s[left]]
                left += 1
                
            if s_count == p_count:
                result.append(left)
                
        return result

        
        
