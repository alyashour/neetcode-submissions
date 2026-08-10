class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = {}
        def str_to_fset(s: str):
            if s in cache:
                return cache[s]

            d = {}
            for char in s:
                d[char] = d.get(char, 0) + 1

            d = frozenset(d.items())
            cache[s] = d

            return d


        groups = {}

        for s in strs:
            d = str_to_fset(s)
            if d in groups:
                groups[d].append(s)
            else:
                groups[d] = [s]
        
        return list(groups.values())


