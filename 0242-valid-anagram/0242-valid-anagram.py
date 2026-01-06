class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False
        letter_map = {}
        for char in s:
            letter_map[char] = letter_map.get(char,0)+1
        for char in t:
            a = letter_map.get(char,0)
            if not a:
                return False
            letter_map[char]-=1
            if letter_map[char]==0:
                del letter_map[char]

        return False if letter_map else True
        