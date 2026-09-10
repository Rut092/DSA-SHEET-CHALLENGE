import collections
class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        occ_map = collections.defaultdict(int)
        count = i = 0 
        for j in range(l):
            occ_map[s[j]]+=1
            
            while(len(occ_map)>=3):
                count+= l-j
                occ_map[s[i]]-=1
                if occ_map[s[i]]==0:
                    del occ_map[s[i]]                
                i+=1

        return count
            
