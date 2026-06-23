class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        i = 0
        s_dict = {}
        while i < len(s):
            if s[i] not in s_dict:
                s_dict[s[i]] = 1
            else:
                s_dict[s[i]] += 1
            i += 1

        i = 0
        t_dict = {}
        while i < len(t):
            if t[i] not in t_dict:
                t_dict[t[i]] = 1
            else:
                t_dict[t[i]] += 1
            i += 1

        return s_dict == t_dict
        