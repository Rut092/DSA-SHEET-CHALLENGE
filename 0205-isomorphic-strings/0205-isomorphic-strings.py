class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return s
        start_map = {}
        reverse_map = {}

        for char_s,char_t in zip(s,t):
            if char_s not in start_map and char_t not in reverse_map:
                start_map[char_s]=char_t
                reverse_map[char_t]=char_s
            elif char_s in start_map and char_t in reverse_map:
                if start_map[char_s]!=char_t or reverse_map[char_t]!=char_s:
                    return False
            else:
                return False
            # print(start_map,reverse_map)
        return True

            