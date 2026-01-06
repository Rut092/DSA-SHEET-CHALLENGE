class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False
        letter_map = {}
        for char in s:
            if char not in letter_map: letter_map[char]=0
            letter_map[char]+=1
        for char in t:
            if char not in letter_map or letter_map[char] ==0: return False
            letter_map[char]-=1

        return True
        