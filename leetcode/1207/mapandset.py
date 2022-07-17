import collections

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = collections.defaultdict(int)
        for i in arr:
            c[i] += 1
        
        x = list(c.values())
        
        return len(x) == len(set(x))