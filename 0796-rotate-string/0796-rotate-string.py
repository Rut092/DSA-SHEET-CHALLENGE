class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        l_needle = len(s)
        if l_needle!=len(goal): return False

        heystack = goal + goal
        needle = s
        lps = [0]*l_needle

        prevLPS , counter = 0,1
        while(counter<l_needle):
            if needle[counter]==needle[prevLPS]:
                lps[counter] = prevLPS + 1
                prevLPS+=1
                counter+=1
            elif prevLPS==0:
                lps[counter]=0
                counter+=1
            else:
                prevLPS = lps[prevLPS-1]


        h_counter,n_counter=0,0
        while(h_counter<len(heystack)):
            if heystack[h_counter]==needle[n_counter]:
                h_counter+=1
                n_counter+=1
            else:
                if n_counter==0:
                    h_counter+=1
                else:
                    n_counter = lps[n_counter-1]
            if n_counter == len(needle):
                return True

        return False



