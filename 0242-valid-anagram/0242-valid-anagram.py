class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False
        letter_map = {}
        for char in s:
            letter_map[char] = letter_map.get(char,0)+1
        for char in t:
            if char not in letter_map or letter_map[char] ==0:
                return False
            letter_map[char]-=1

        return True
        