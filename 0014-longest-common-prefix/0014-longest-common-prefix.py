class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i=0
        letter = ""
        for i in range(len(strs[0])):
            letter = strs[0][i]
            for word in strs:
                if i>len(word)-1 or word[i]!=letter:
                    return strs[0][:i]
            i+=1
        return strs[0][:i]
