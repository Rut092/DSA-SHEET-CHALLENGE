class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        freq_map = {}
        for i in t:
            if i not in freq_map:
                freq_map[i]=1
            else:
                freq_map[i]+=1
        
        i = 0
        min_i,min_j=0,float('inf')
        for j in range(len(s)):
            if s[j] in freq_map:
                freq_map[s[j]]-=1
            else:
                freq_map[s[j]]=-2
        
            is_true = True
            for char in freq_map:
                if freq_map[char]>0:
                    is_true = False
                    break
            while(is_true and freq_map[s[i]]+1<=0):
                freq_map[s[i]]+=1
                i+=1

            if min_j-min_i>j-i and is_true:
                min_i,min_j=i,j

        return s[min_i:min_j+1] if min_j!=float('inf') else ""
            
