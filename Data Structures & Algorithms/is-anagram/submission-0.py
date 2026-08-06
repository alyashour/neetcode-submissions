class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        h = {}
        for i, s_char in enumerate(s):
            t_char = t[i]

            h[s_char] = h.get(s_char, 0) + 1
            h[t_char] = h.get(t_char, 0) - 1
        
        print(h)
        for _, i in h.items():
            if i != 0:
                return False
        
        return True
